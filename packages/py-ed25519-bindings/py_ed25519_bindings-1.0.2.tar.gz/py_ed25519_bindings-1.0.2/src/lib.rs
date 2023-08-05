// Python ed25519 Bindings
//
// Copyright 2018-2020 Stichting Polkascan (Polkascan Foundation).
//
// Licensed under the Apache License, Version 2.0 (the "License");
// you may not use this file except in compliance with the License.
// You may obtain a copy of the License at
//
// http://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS IS" BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License.

//! Python bindings for the ed25519-dalek RUST crate.
//!
//! py-ed25519-bindings provides bindings to the Rust create
//! [ed25519-dalek](https://crates.io/crates/ed25519-dalek), allowing for some limited
//! use and management of ed25519 elliptic keys.

use pyo3::prelude::*;
use pyo3::types::{PyBytes, PyTuple};
use pyo3::{wrap_pyfunction, IntoPy, PyObject, exceptions};
use std::convert::TryFrom;
use ed25519_dalek::{Keypair, PublicKey, SecretKey, Signature, Verifier, Signer};

pub struct PyKeypair([u8; 32], [u8; 32]);
pub struct PySignature([u8; 64]);

pub const SEED_KEY_LENGTH: usize = 32;

/// Keypair helper function.
fn create_from_pair(pair: &[u8]) -> PyResult<Keypair> {
	match Keypair::from_bytes(pair) {
		Ok(pair) => Ok(pair),
		Err(_) => Err(exceptions::ValueError::py_err("Provided pair is invalid."))
	}
}

/// Keypair helper function
fn create_from_parts(public: &[u8], secret: &[u8]) -> PyResult<Keypair> {
	let mut pair = vec![];

	pair.extend_from_slice(secret);
	pair.extend_from_slice(public);

	create_from_pair(&pair)
}

/// Keypair helper function.
fn create_from_seed(seed: &[u8]) -> PyResult<Keypair> {

	if seed.len() != SEED_KEY_LENGTH {
		return Err(exceptions::ValueError::py_err(
			format!("Expected bytes of length {}, got {}", SEED_KEY_LENGTH, seed.len()))
		)
	}

	let secret = SecretKey::from_bytes(seed).unwrap();

	let public: PublicKey = (&secret).into();

	create_from_parts(public.as_bytes(), seed)
}

/// PublicKey helper
fn create_public(public: &[u8]) -> PublicKey {
	match PublicKey::from_bytes(public) {
		Ok(public) => return public,
		Err(_) => panic!("Provided public key is invalid.")
	}
}

/// Returns a public and private key pair from the given 32-byte seed.
///
/// # Arguments
///
/// * `seed` - A 32 byte seed.
///
/// # Returns
///
/// A tuple containing the 32-byte secret key and 32-byte public key, in that order.
#[pyfunction]
#[text_signature = "(seed)"]
pub fn ed_from_seed(seed: &[u8]) -> PyResult<PyKeypair> {

	let keypair = match create_from_seed(seed) {
		Ok(keypair) => keypair,
		Err(err) =>  return Err(err)
	};

	Ok(PyKeypair(keypair.secret.to_bytes(), keypair.public.to_bytes()))

}

/// Signs a message with the given keypair, returning the resulting signature.
///
/// # Arguments
///
/// * `public` - The ed25519 public key, as an array of 32 bytes
/// * `secret` - The ed25519 private key, as an array of 32 bytes
/// * `message` - The binary message to sign.
///
/// # Returns
///
/// A 64-byte signature.
#[pyfunction]
#[text_signature = "(public, secret, message)"]
pub fn ed_sign(public: &[u8], secret: &[u8], message: &[u8]) -> PyResult<PySignature> {

	let keypair = match create_from_parts(public, secret) {
		Ok(keypair) => keypair,
		Err(err) => return Err(err)
	};

	Ok(PySignature(keypair.sign(message).to_bytes()))
}

/// Verifies that a signature on a given message was generated by private key
/// corresponding to the specified public key.
///
/// # Arguments
///
/// * `signature` - The 64-byte ed25519 signature.
/// * `message` - The binary message on which to verify the signature.
/// * `public` - The ed25519 public key, as an array of 32 bytes
///
/// # Returns
///
/// True if the signature is valid, false otherwise.
#[pyfunction]
#[text_signature = "(signature, message, public)"]
pub fn ed_verify(signature: &[u8], message: &[u8], public: &[u8]) -> bool {
	let signature = match Signature::try_from(signature) {
		Ok(signature) => signature,
		Err(_) => return false
	};

	create_public(public)
		.verify(message, &signature)
		.is_ok()
}


/// This module is a Python module implemented in Rust.
#[pymodule]
fn ed25519_dalek(_py: Python<'_>, m: &PyModule) -> PyResult<()> {
    m.add_wrapped(wrap_pyfunction!(ed_from_seed))?;
    m.add_wrapped(wrap_pyfunction!(ed_sign))?;
    m.add_wrapped(wrap_pyfunction!(ed_verify))?;

    Ok(())
}

// Convert Keypair object to a Python Keypair tuple
impl IntoPy<PyObject> for PyKeypair {
    fn into_py(self, py: Python) -> PyObject {
        let secret = PyBytes::new(py, &self.0);
        let public = PyBytes::new(py, &self.1);

        PyTuple::new(py, vec![secret, public]).into_py(py)
    }
}

// Convert Keypair object to a Python Keypair tuple
impl IntoPy<PyObject> for PySignature {
    fn into_py(self, py: Python) -> PyObject {
        let sig = PyBytes::new(py, &self.0);
        sig.into_py(py)
    }
}
