from nacl_service.server import generate_hash

INPUT_MESSAGE = "TEST INPUT MESSAGE"

def test_generate_hash_sha256_hexadecimal():
    result = generate_hash(INPUT_MESSAGE, "SHA256").text
    assert result == "ab1ba9a35f85c47a5d5bf848547807b5e7c08c033ad332066cabf03caba32fae"

def test_generate_hash_sha512_hexadecimal():
    result = generate_hash(INPUT_MESSAGE, "SHA512").text
    assert result == "a2ba191743f99069b5cfa5cf32c8b0787bff5e40f089abb4e01be9da75e1adc24cdf4e0ccbbe3e1ff4c481db8431c8678d4bca7e85867a8ab2b7e5d11348c2fa"

def test_generate_hash_sha256_output_base64():
    result = generate_hash(INPUT_MESSAGE, "SHA256", "Base64").text
    assert result == "qxupo1+FxHpdW/hIVHgHtefAjAM60zIGbKvwPKujL64="

def test_generate_hash_sha512_output_base64():
    result = generate_hash(INPUT_MESSAGE, "SHA512", "Base64").text
    assert result == "oroZF0P5kGm1z6XPMsiweHv/XkDwiau04Bvp2nXhrcJM304My74+H/TEgduEMchnjUvKfoWGeoqyt+XRE0jC+g=="