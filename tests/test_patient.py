"""Tests for the Patient model."""


def test_create_patient():
    from inflammation.models import Patient

    name = 'Alice'
    p = Patient(name=name)

    assert p.name == name

def test_create_doctor():
    from inflammation.models import Doctor

    name = 'Alice'
    d = Doctor(name=name)

    assert d.name == name

def test_add_patients_to_doctor():
    from inflammation.models import Patient, Doctor

    name = 'Alice'
    p = Patient(name=name)

    name = 'Jane'
    d = Doctor(name=name)
    d.add_patient(p)
    assert d.get_patients[0] == p
