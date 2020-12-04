import pytest

def serve_beer(age):
  if (age<18):
    return "No beer"
  else:
    return "Have beer"


def test_serve_beer_legal():
  adult = 25
  assert serve_beer(adult) == "Have beer"

def test_serve_beer_illegal():
  child = 30
  assert serve_beer(child) == "No beer"