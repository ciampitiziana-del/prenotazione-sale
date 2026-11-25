"""Test della classe Agenda."""

import unittest
from datetime import date, timedelta

from prenotazioni import (
    ORIZZONTE_GIORNI,
    Agenda,
    DataNonAmmessa,
    Prenotazione,
    PrenotazioneNonTrovata,
    Sala,
    SalaNonTrovata,
)


class TestAgenda(unittest.TestCase):
    def setUp(self):
        self.oggi = date(2026, 11, 10)
        self.agenda = Agenda()
        self.agenda.aggiungi_sala(Sala("A2", "Aula 2", 25))

    def test_sala_duplicata(self):
        with self.assertRaises(ValueError):
            self.agenda.aggiungi_sala(Sala("A2", "Altra sala", 15))

    def test_sala_inesistente(self):
        with self.assertRaises(SalaNonTrovata):
            self.agenda.sala("X1")

    def test_date_non_ammesse(self):
        casi = [
            self.oggi - timedelta(days=1),
            date(2026, 11, 15),
            self.oggi + timedelta(days=ORIZZONTE_GIORNI + 2),
        ]
        for giorno in casi:
            with self.subTest(giorno=giorno):
                prenotazione = Prenotazione("A2", giorno, "09:00", "10:00", "Rossi", 5)
                with self.assertRaises(DataNonAmmessa):
                    self.agenda.prenota(prenotazione, oggi=self.oggi)

    def test_prenota_oggi(self):
        prenotazione = Prenotazione("A2", self.oggi, "09:00", "10:00", "Rossi", 5)

        identificativo = self.agenda.prenota(prenotazione, oggi=self.oggi)

        self.assertIs(self.agenda.prenotazione(identificativo), prenotazione)

    def test_cancella_id_inesistente(self):
        with self.assertRaises(PrenotazioneNonTrovata):
            self.agenda.cancella(99)

    def test_prenotazione_id_inesistente(self):
        with self.assertRaises(PrenotazioneNonTrovata):
            self.agenda.prenotazione(99)


if __name__ == "__main__":
    unittest.main()
