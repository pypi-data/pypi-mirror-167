use pyo3::prelude::*;
use rocksdb::{DBWithThreadMode, MultiThreaded};
use std::path::Path;
use std::sync::Arc;
use std::fs;
extern crate rocksdb;


#[pyclass]
#[derive(Clone)]
pub struct RocksDB {
    pub db: Arc<DBWithThreadMode<MultiThreaded>>
}
    #[pymethods]
    impl RocksDB {
    #[new]
    fn new(path: &str) -> Self {
// create directory and all parent directory
        if !Path::new(path).exists() {
            match fs::create_dir_all(path) {
                Ok(_) => {},
                Err(_error) => panic!("Failed to create directory at {}.", path)
            };
        }
// TODO: create options class
// TODO: optimize options in python
    let mut opts = rocksdb::Options::default();
    opts.create_if_missing(true);
    opts.increase_parallelism(24);

        let database = match DBWithThreadMode::open(&opts, path) {
            Ok(r) => r,
            Err(e) => panic!("Unable to open RocksDB at {}, error: {}",path, e)
        };
        RocksDB {
            db: Arc::new(database)
        }

    }

    fn put(&self, header: String, sequence: String) {
        self.db.put(header.as_bytes(), sequence.as_bytes()).unwrap();
    }

    fn get(&self, header: String) -> Option<String> {
        let sequence = match self.db.get(header.as_bytes()) {
            Ok(Some(r)) => String::from_utf8(r).unwrap(),
            Ok(None) => return None,
            Err(e) => panic!("Received database error when trying to retrieve sequence, error: {}", e)
        };

        Some(sequence)
    }

    fn delete(&self, header: String) -> bool {
        self.db.delete(header.as_bytes()).is_ok()
    }

    fn batch_put(&self, inserts: Vec<Vec<String>>) -> u64 {
        let mut batch = rocksdb::WriteBatch::default();
        let mut counter: u64 = 0;
        for pair in inserts.iter() {
            batch.put(pair[0].as_bytes(), pair[1].as_bytes());
            counter += 1
        }
        match self.db.write(batch) {
            Ok(_) => counter,
            Err(_) => 0
        }
    }
    fn batch_get(&self, keys: Vec<String>) -> Vec<String> {
        let byte_keys: Vec<&[u8]> = keys.iter().map(|x| x.as_bytes()).collect();
        let packed_results = self.db.multi_get(byte_keys.iter());
        let mut unpacked_results: Vec<String> = Vec::with_capacity(keys.capacity());
        for pack in packed_results.iter() {
            match pack {
                Ok(Some(value)) => unpacked_results.push(String::from_utf8(value.to_vec()).unwrap()),
                Ok(None) => unpacked_results.push( String::from("")),
                Err(_) => unpacked_results.push(String::from("error")),
            }
        }
        return unpacked_results;
    }
}

/// A Python module that wraps rocksdb's rust crate.
#[pymodule]
fn wrap_rocks(_py: Python, m: &PyModule) -> PyResult<()> {
    m.add_class::<RocksDB>()?;
    Ok(())
}