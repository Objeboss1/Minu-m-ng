"""Mängu helid — taustamuusika ja efektid."""
import array
import math
import os

import pygame

#Helifailide kaust (projekti juures)
HAALID_KAUST = "hääled"
_BASE = os.path.dirname(os.path.abspath(__file__))

FAIL_MUUSIKA = "mixkit-morning-birds-2472.wav"
FAIL_NUPP = "mixkit-fast-double-click-on-mouse-275.wav"
FAIL_OST = "mixkit-clinking-coins-1993.wav"


def _tee(failinimi):
    return os.path.join(_BASE, HAALID_KAUST, failinimi)


def _loo_loks_haal():
    """Lühike „tõrts“ kui eraldi loks.wav puudub."""
    sample_rate = 22050
    duration = 0.09
    n_samples = int(sample_rate * duration)
    buf = array.array("h")
    for i in range(n_samples):
        t = i / sample_rate
        amp = int(
            28000
            * math.exp(-t * 45)
            * (0.6 + 0.4 * math.sin(2 * math.pi * 90 * t))
        )
        buf.append(amp)
        buf.append(amp)
    return pygame.mixer.Sound(buffer=bytes(buf))


class Helid:
    def __init__(self):
        if not pygame.mixer.get_init():
            pygame.mixer.init()
        self.snd_nupp = None
        self.snd_loks = None
        self.snd_ost = None
        self._laadi()

    def _laadi(self):
        #taustamuusika (vaikne, kordub)
        try:
            pygame.mixer.music.load(_tee(FAIL_MUUSIKA))
            pygame.mixer.music.set_volume(0.18)
            pygame.mixer.music.play(-1)
        except pygame.error:
            pass

        try:
            self.snd_nupp = pygame.mixer.Sound(_tee(FAIL_NUPP))
            self.snd_nupp.set_volume(0.45)
        except pygame.error:
            self.snd_nupp = None

        try:
            self.snd_ost = pygame.mixer.Sound(_tee(FAIL_OST))
            self.snd_ost.set_volume(0.55)
        except pygame.error:
            self.snd_ost = None

        loks_tee = _tee("loks.wav")
        if os.path.isfile(loks_tee):
            try:
                self.snd_loks = pygame.mixer.Sound(loks_tee)
                self.snd_loks.set_volume(0.65)
            except pygame.error:
                self.snd_loks = _loo_loks_haal()
        else:
            self.snd_loks = _loo_loks_haal()
            self.snd_loks.set_volume(0.65)

    def play_nupp(self):
        if self.snd_nupp:
            self.snd_nupp.play()

    def play_loks(self):
        if self.snd_loks:
            self.snd_loks.play()

    def play_ost(self):
        if self.snd_ost:
            self.snd_ost.play()
