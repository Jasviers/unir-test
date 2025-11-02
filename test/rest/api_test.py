import http.client
import os
import unittest
from urllib.request import urlopen
from urllib.error import HTTPError

import pytest

BASE_URL = os.environ.get("BASE_URL")
DEFAULT_TIMEOUT = 2  # in secs


@pytest.mark.api
class TestApi(unittest.TestCase):
    def setUp(self):
        self.assertIsNotNone(BASE_URL, "URL no configurada")
        self.assertTrue(len(BASE_URL) > 8, "URL no configurada")

    def test_api_add(self):
        url = f"{BASE_URL}/calc/add/2/2"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(
            response.status, http.client.OK, f"Error en la petición API a {url}"
        )

    def test_api_substract(self):
        url = f"{BASE_URL}/calc/substract/2/2"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(
            response.status, http.client.OK, f"Error en la petición API a {url}"
        )

    def test_api_multiply(self):
        url = f"{BASE_URL}/calc/multiply/2/2"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(
            response.status, http.client.OK, f"Error en la petición API a {url}"
        )

    def test_api_divide(self):
        url = f"{BASE_URL}/calc/divide/2/2"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(
            response.status, http.client.OK, f"Error en la petición API a {url}"
        )

    def test_api_power(self):
        url = f"{BASE_URL}/calc/power/2/2"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(
            response.status, http.client.OK, f"Error en la petición API a {url}"
        )

    def test_api_root(self):
        url = f"{BASE_URL}/calc/root/9"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(
            response.status, http.client.OK, f"Error en la petición API a {url}"
        )

    def test_api_logBase10(self):
        url = f"{BASE_URL}/calc/logBase10/100"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(
            response.status, http.client.OK, f"Error en la petición API a {url}"
        )

    ### API type errors ###

    def test_error_api_add(self):
        url = f"{BASE_URL}/calc/add/2/a"
        try:
            urlopen(url, timeout=DEFAULT_TIMEOUT)
            self.fail(f"Se esperaba un error en la petición a: {url}")
        except HTTPError as e:
            self.assertEqual(
                e.code,
                http.client.BAD_REQUEST,
                f"Fallo corectamente la petición API a {url}",
            )

    def test_error_api_substract(self):
        url = f"{BASE_URL}/calc/substract/2/a"
        try:
            urlopen(url, timeout=DEFAULT_TIMEOUT)
            self.fail(f"Se esperaba un error en la petición a: {url}")
        except HTTPError as e:
            self.assertEqual(
                e.code,
                http.client.BAD_REQUEST,
                f"Fallo corectamente la petición API a {url}",
            )

    def test_error_api_multiply(self):
        url = f"{BASE_URL}/calc/multiply/2/a"
        try:
            urlopen(url, timeout=DEFAULT_TIMEOUT)
            self.fail(f"Se esperaba un error en la petición a: {url}")
        except HTTPError as e:
            self.assertEqual(
                e.code,
                http.client.BAD_REQUEST,
                f"Fallo corectamente la petición API a {url}",
            )

    def test_error_api_divide(self):
        url = f"{BASE_URL}/calc/divide/a/2"
        try:
            urlopen(url, timeout=DEFAULT_TIMEOUT)
            self.fail(f"Se esperaba un error en la petición a: {url}")
        except HTTPError as e:
            self.assertEqual(
                e.code,
                http.client.BAD_REQUEST,
                f"Fallo corectamente la petición API a {url}",
            )

    def test_error_api_divide_by_0(self):
        url = f"{BASE_URL}/calc/divide/a/0"
        try:
            urlopen(url, timeout=DEFAULT_TIMEOUT)
            self.fail(f"Se esperaba un error en la petición a: {url}")
        except HTTPError as e:
            self.assertEqual(
                e.code,
                http.client.BAD_REQUEST,
                f"Fallo corectamente la petición API a {url}",
            )

    def test_error_api_power(self):
        url = f"{BASE_URL}/calc/power/2/a"
        try:
            urlopen(url, timeout=DEFAULT_TIMEOUT)
            self.fail(f"Se esperaba un error en la petición a: {url}")
        except HTTPError as e:
            self.assertEqual(
                e.code,
                http.client.BAD_REQUEST,
                f"Fallo corectamente la petición API a {url}",
            )

    def test_error_api_root(self):
        url = f"{BASE_URL}/calc/root/b"
        try:
            urlopen(url, timeout=DEFAULT_TIMEOUT)
            self.fail(f"Se esperaba un error en la petición a: {url}")
        except HTTPError as e:
            self.assertEqual(
                e.code,
                http.client.BAD_REQUEST,
                f"Fallo corectamente la petición API a {url}",
            )

    def test_error_api_root_no_negative(self):
        url = f"{BASE_URL}/calc/root/-10"
        try:
            urlopen(url, timeout=DEFAULT_TIMEOUT)
            self.fail(f"Se esperaba un error en la petición a: {url}")
        except HTTPError as e:
            self.assertEqual(
                e.code,
                http.client.BAD_REQUEST,
                f"Fallo corectamente la petición API a {url}",
            )

    def test_error_api_logBase10(self):
        url = f"{BASE_URL}/calc/logBase10/10fa"
        try:
            urlopen(url, timeout=DEFAULT_TIMEOUT)
            self.fail(f"Se esperaba un error en la petición a: {url}")
        except HTTPError as e:
            self.assertEqual(
                e.code,
                http.client.BAD_REQUEST,
                f"Fallo corectamente la petición API a {url}",
            )
