"""Test di regressione per i difetti segnalati."""

import unittest
from datetime import date

from prenotazioni import Agenda, Prenotazione, Sala


class TestSegnalazioni(unittest.TestCase):
    def test_prenotazioni_contigue(self):
        oggi = date(2026, 11, 10)
        agenda = Agenda()
        agenda.aggiungi_sala(Sala("A2", "Aula 2", 25))
        prima = Prenotazione("A2", oggi, "09:00", "10:00", "Rossi", 5)
        seconda = Prenotazione("A2", oggi, "10:00", "11:00", "Bianchi", 5)
        agenda.prenota(prima, oggi=oggi)

        identificativo = agenda.prenota(seconda, oggi=oggi)

        self.assertIs(agenda.prenotazione(identificativo), seconda)


if __name__ == "__main__":
    unittest.main()

    def test_prenotazione_a_capienza_massima(self):
        oggi = date(2026, 11, 10)
        agenda = Agenda()
        agenda.aggiungi_sala(Sala("R1", "Sala riunioni", 10))
        prenotazione = Prenotazione("R1", oggi, "09:00", "10:00", "Rossi", 10)

        identificativo = agenda.prenota(prenotazione, oggi=oggi)

        self.assertIs(agenda.prenotazione(identificativo), prenotazione)
