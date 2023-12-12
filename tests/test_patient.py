"""Tests for the Patient model."""
from inflammation.models import Patient, Doctor, Person


def test_create_patient():
    name = 'Alice'
    p = Patient(name=name)

    assert p.name == name


def test_create_doctor():
    name = 'Alice'
    d = Doctor(name=name)

    assert d.name == name


def test_patient_type():
    name = 'Alice'
    p = Patient(name)
    assert isinstance(p, Person)


def test_doctor_type():
    name = 'Alice'
    d = Doctor(name)
    assert isinstance(d, Person)


def test_add_patient():
    d = Doctor('Alice')
    p = Patient('Alice')
    d.add_patient(p)
    assert len(d.patients) == 1


def test_no_duplicate_patient():
    d = Doctor('Alice')
    p = Patient('Alice')
    d.add_patient(p)
    d.add_patient(p)
    assert len(d.patients) == 1
