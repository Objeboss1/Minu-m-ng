"""Tähtsaim osa mängus. (Puu tüvi), Juhib mängu"""
import pygame

from Väärtused import *
from Helid import Helid

class Game:

    def __init__(self):

        # Käivitab pygame
        pygame.init()

        #helid (taust + efektid)
        self.haalid = Helid()

        # Loob akna
        self.screen = pygame.display.set_mode(
            (SCREEN_WIDTH, SCREEN_HEIGHT)
        )

        # Akna nimi
        pygame.display.set_caption("Karli peksmine Beta 1.0 (Lihtsustatud versioon)")

        # Kas mäng töötab?
        self.running = True

        #poe skinnide ja taustapiltide nupude asukoht
        self.pood_vaade = "valik"
        self.pood_skinid_rect = pygame.Rect(200, 320, 200, 56)
        self.pood_taust_rect = pygame.Rect(420, 320, 200, 56)

        #poe nupp
        self.pood_rect = pygame.Rect(20, 20, 120, 44)

        #tagasi nupp
        self.tagasi_rect = pygame.Rect(20, 20, 140, 44)

        #upgrade nupp
        self.upgrade_rect = pygame.Rect(160, 20, 140, 44)

        #sissejuhtus
        self.olek = "sissejuhatus"
        self.jargmine_rect = pygame.Rect(0, 0, 160, 48)
        self.jargmine_rect.bottomright = (SCREEN_WIDTH - 20, SCREEN_HEIGHT - 20)

        #lõpeta mäng väärtused
        self.lopeta_hind_raha = 800
        self.lopeta_hind_token = 35
        self.lopeta_rect = pygame.Rect(0, 0, 280, 48)
        self.lopeta_rect.bottomright = (SCREEN_WIDTH - 20, SCREEN_HEIGHT - 20)


        #upgrade loendur
        self.raha_kliku = 1.0
        self.upgrade_kliku_tase = 0
        self.upgrade_kliku_max_tase = 10

        #passiivne income
        self.passiivne_tase = 0
        self.passiivne_max_tase = 19
        self.passiivne_viimane_aeg = pygame.time.get_ticks()

        #raha loendur
        self.klikke_pildile = 1
        #Raha
        self.raha = 0
        #Tokenid
        self.parem_raha = 0
        self.font = pygame.font.SysFont("Arial", 28)

#_______________________________________________________________________________________________________________________________________________________________
        """Uued skinnid ja taustapildid."""

        #skinnid
        self.skinid_info = [
            {"nimi": "Karl Kiipus", "tee": "Karl Kiipus1.png", "hind": 0},
            {"nimi": "Putin", "tee": "Skinnid/Putin.png", "hind": 5},
            {"nimi": "Trump", "tee": "Skinnid/Trump.png", "hind": 10},
            {"nimi": "Netanjahu", "tee": "Skinnid/Benjamin.png", "hind": 15},
            {"nimi": "Alar Karis", "tee": "Skinnid/Alar.png", "hind": 20},
        ]
        self.skin_pinnad = []
        for info in self.skinid_info:
            p = pygame.image.load(info["tee"]).convert_alpha()
            self.skin_pinnad.append(p)
        self.valitud_skin = 0
        self.ostetud_skinid = {0}
        self.pilt = self.skin_pinnad[0]
        self.pildi_rect = self.pilt.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))

        # Iga rea „Osta / Vali“ nupp (paremal)
        self.skin_nupu_rectid = []
        rida_y = 110
        for _ in self.skinid_info:
            self.skin_nupu_rectid.append(
                pygame.Rect(SCREEN_WIDTH - 180, rida_y, 140, 44)
            )
            rida_y += 86


        #Taustapildid
        self.taustad_info = [
            {"nimi": "Kosmos", "tee": "Taustad/Kosmos.png", "hind_token": 1},
            {"nimi": "Loodus", "tee": "Taustad/Loodus.png", "hind_token": 1},
            {"nimi": "Mästik", "tee": "Taustad/Mäestik.png", "hind_token": 1},
            {"nimi": "Rand", "tee": "Taustad/Rand.png", "hind_token": 1},
        ]
        self.tausta_pinnad = []
        for info in self.taustad_info:
            self.tausta_pinnad.append(pygame.image.load(info["tee"]).convert_alpha())
        self.valitud_taust = 0
        self.ostetud_taustad = {0}
        self.tausta_pind = self.tausta_pinnad[0]
        self.taust_nupu_rectid = []
        rida_y = 110
        for _ in self.taustad_info:
            self.taust_nupu_rectid.append(
                pygame.Rect(SCREEN_WIDTH - 180, rida_y, 140, 44)
            )
            rida_y += 86

        # upgrade nupud ja sellel olevad tekstid
        self.upgrade_info = [
            {
                "nimi": "Tugevam klõps",
                "kirjeldus": "+0,5 € iga klõps (max 10)",
                "hind": 10,
                "tyyp": "klik",
            },
            {
                "nimi": "Automaatne raha",
                "kirjeldus": "Raha iga X sek (kiireneb)",
                "hind": 15,
                "tyyp": "passiivne",
            },
        ]
        self.upgrade_rea_korgus = 90
        self.upgrade_rea_rectid = []
        self.upgrade_nupu_rectid = []
        rida_y = 180
        nupu_w, nupu_h = 140, 44
        for _ in self.upgrade_info:
            self.upgrade_rea_rectid.append(
                pygame.Rect(24, rida_y, SCREEN_WIDTH - 48, self.upgrade_rea_korgus)
            )
            nupu_y = rida_y + (self.upgrade_rea_korgus - nupu_h) // 2
            self.upgrade_nupu_rectid.append(
                pygame.Rect(SCREEN_WIDTH - 180, nupu_y, nupu_w, nupu_h)
            )
            rida_y += 100








    def vali_skin(self, i):
        self.valitud_skin = i
        self.pilt = self.skin_pinnad[i]
        self.pildi_rect = self.pilt.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))

    def vali_taust(self, i):
        self.valitud_taust = i
        self.tausta_pind = self.tausta_pinnad[i]
#_____________________________________________________________________________________________________________________________

    #upgrade loendur iga klikiga -0.5 sec
    def passiivne_intervall_sek(self):
        return max(0.5, 10.0 - self.passiivne_tase * 0.5)

    def passiivne_jargmine_hind(self):
        return 15 + self.passiivne_tase * 5

    def klik_jargmine_hind(self):
        return 10 + self.upgrade_kliku_tase * 2

    def play_nupp(self):
        self.haalid.play_nupp()

    def play_loks(self):
        self.haalid.play_loks()

    def play_ost(self):
        self.haalid.play_ost()


    def run(self):

        # Game loop
        while self.running:

            # Kontrollib evente
            for event in pygame.event.get():

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.olek == "sissejuhatus":
                        if self.jargmine_rect.collidepoint(event.pos):
                            self.play_nupp()
                            self.olek = "mäng"
                    elif self.olek == "mäng":
                        if self.upgrade_rect.collidepoint(event.pos):
                            self.play_nupp()
                            self.olek = "upgrade"
                        elif self.pood_rect.collidepoint(event.pos):
                            self.play_nupp()
                            self.olek = "pood"
                            self.pood_vaade = "valik"
                        elif self.lopeta_rect.collidepoint(event.pos):
                            if (
                                self.raha >= self.lopeta_hind_raha
                                and self.parem_raha >= self.lopeta_hind_token
                            ):
                                self.play_ost()
                                self.raha -= self.lopeta_hind_raha
                                self.parem_raha -= self.lopeta_hind_token
                                self.olek = "lõpp"
                            else:
                                self.play_nupp()
                        elif self.pildi_rect.collidepoint(event.pos):
                            self.play_loks()
                            self.klikke_pildile += 1
                            self.raha += self.raha_kliku
                            if self.klikke_pildile % 10 == 0:
                                self.parem_raha += 1


                    #upgrade nupud jne
                    elif self.olek == "upgrade":
                        if self.tagasi_rect.collidepoint(event.pos):
                            self.play_nupp()
                            self.olek = "mäng"
                        else:
                            for i, nupu_r in enumerate(self.upgrade_nupu_rectid):
                                if not nupu_r.collidepoint(event.pos):
                                    continue
                                info = self.upgrade_info[i]
                                if info["tyyp"] == "klik":
                                    if self.upgrade_kliku_tase >= self.upgrade_kliku_max_tase:
                                        self.play_nupp()
                                        break
                                    hind = self.klik_jargmine_hind()
                                    if self.raha >= hind:
                                        self.play_ost()
                                        self.raha -= hind
                                        self.raha_kliku += 0.5
                                        self.upgrade_kliku_tase += 1
                                    else:
                                        self.play_nupp()
                                elif info["tyyp"] == "passiivne":
                                    if self.passiivne_tase >= self.passiivne_max_tase:
                                        self.play_nupp()
                                        break
                                    hind = self.passiivne_jargmine_hind()
                                    if self.raha >= hind:
                                        self.play_ost()
                                        self.raha -= hind
                                        self.passiivne_tase += 1
                                        self.passiivne_viimane_aeg = pygame.time.get_ticks()
                                    else:
                                        self.play_nupp()
                                break



                    elif self.olek == "pood":
                        if self.pood_vaade == "valik":
                            if self.pood_skinid_rect.collidepoint(event.pos):
                                self.play_nupp()
                                self.pood_vaade = "skinnid"
                            elif self.pood_taust_rect.collidepoint(event.pos):
                                self.play_nupp()
                                self.pood_vaade = "taust"
                            elif self.tagasi_rect.collidepoint(event.pos):
                                self.play_nupp()
                                self.olek = "mäng"
                        elif self.pood_vaade == "skinnid":
                            if self.tagasi_rect.collidepoint(event.pos):
                                self.play_nupp()
                                self.pood_vaade = "valik"
                            else:
                                for i, nupu_r in enumerate(self.skin_nupu_rectid):
                                    if nupu_r.collidepoint(event.pos):
                                        hind = self.skinid_info[i]["hind"]
                                        if i in self.ostetud_skinid or hind == 0:
                                            self.play_nupp()
                                            self.vali_skin(i)
                                        elif self.raha >= hind:
                                            self.play_ost()
                                            self.raha -= hind
                                            self.ostetud_skinid.add(i)
                                            self.vali_skin(i)
                                        else:
                                            self.play_nupp()
                                        break
                        elif self.pood_vaade == "taust":
                            if self.tagasi_rect.collidepoint(event.pos):
                                self.play_nupp()
                                self.pood_vaade = "valik"
                            else:
                                for i, nupu_r in enumerate(self.taust_nupu_rectid):
                                    if nupu_r.collidepoint(event.pos):
                                        hind_t = self.taustad_info[i]["hind_token"]
                                        if i in self.ostetud_taustad or hind_t == 0:
                                            self.play_nupp()
                                            self.vali_taust(i)
                                        elif self.parem_raha >= hind_t:
                                            self.play_ost()
                                            self.parem_raha -= hind_t
                                            self.ostetud_taustad.add(i)
                                            self.vali_taust(i)
                                        else:
                                            self.play_nupp()
                                        break

                    #lõpuekraan / sulge mäng
                    elif self.olek == "lõpp":
                        if self.tagasi_rect.collidepoint(event.pos):
                            self.play_nupp()
                            self.running = False

                # Kui vajutatakse X nuppu
                if event.type == pygame.QUIT:
                    self.running = False

            #passiivne raha
            if self.olek == "mäng" and self.passiivne_tase > 0:
                nüüd = pygame.time.get_ticks()
                ms = self.passiivne_intervall_sek() * 1000
                if nüüd - self.passiivne_viimane_aeg >= ms:
                    self.raha += 1
                    self.passiivne_viimane_aeg = nüüd



            # Taust mustaks
            self.screen.fill("black")

            #sissejuhatuse pilt


            #Pealkiri
            if self.olek == "sissejuhatus":

                # 1.rida
                rida2 = self.font.render("Karl_studio presents:", True, (255, 255, 255))
                r2_rect = rida2.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 3))

                # 3. rida
                rida3 = self.font.render("Tehtud ChatGPT & Cursor abiga", True, (255, 255, 255))
                r3_rect = rida3.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 3 + 90))

                # 4. rida
                rida4 = self.font.render("Kuidas mängida?", True, (255, 255, 255))
                r4_rect = rida4.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 3 + 160))

                # 5. rida
                rida5 = self.font.render("Karl on olnud väga paha poiss…\nSinu ülesanne on talle peksa anda ja teenida selle eest Raha ning Tokeneid \nRaha ja Tokenite eest saad osta upgrade’e ja muud", True, (255, 255, 255))
                r5_rect = rida5.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 3 + 230))

                # 6. rida
                rida6 = self.font.render(
                    "Klikki Järgmine et anda Karlile peksa",
                    True, (255, 255, 255))
                r6_rect = rida6.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 3 + 485))

                pealkiri = self.font.render("Karli peksmine Beta 1.0 (Lihtsustatud versioon)", True, (255, 255, 255))
                pr = pealkiri.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 3 + 40))
                self.screen.blit(rida3, r3_rect)
                self.screen.blit(rida4, r4_rect)
                self.screen.blit(rida5, r5_rect)
                self.screen.blit(rida6, r6_rect)



                self.screen.blit(rida2, r2_rect)
                self.screen.blit(pealkiri, pr)
                pygame.draw.rect(self.screen, (80, 80, 80), self.jargmine_rect)
                nupu_tekst = self.font.render("Järgmine", True, (255, 255, 255))
                ntr = nupu_tekst.get_rect(center=self.jargmine_rect.center)
                self.screen.blit(nupu_tekst, ntr)


            #Mängu pilt
            elif self.olek == "mäng":
                taust_suur = pygame.transform.scale(
                    self.tausta_pind, (SCREEN_WIDTH, SCREEN_HEIGHT)
                )
                self.screen.blit(taust_suur, (0, 0))
                self.screen.blit(self.pilt, self.pildi_rect)
                tekst = self.font.render(f"Raha: {self.raha:.1f}", True, (255, 255, 255))
                teksti_rect = tekst.get_rect(topright=(SCREEN_WIDTH - 10, 10))
                self.screen.blit(tekst, teksti_rect)
                tekst2 = self.font.render(f"Tokenid: {self.parem_raha}", True, (255, 255, 255))
                tekst2_rect = tekst2.get_rect(topright=(SCREEN_WIDTH - 10, 40))
                self.screen.blit(tekst2, tekst2_rect)

                #upgrade nupp
                pygame.draw.rect(self.screen, (120, 90, 40), self.upgrade_rect)
                up_txt = self.font.render("Upgrade", True, (255, 255, 255))
                self.screen.blit(up_txt, up_txt.get_rect(center=self.upgrade_rect.center))

                #poe nupp
                pygame.draw.rect(self.screen, (60, 120, 60), self.pood_rect)
                pood_tekst = self.font.render("Pood", True, (255, 255, 255))
                ptr = pood_tekst.get_rect(center=self.pood_rect.center)
                self.screen.blit(pood_tekst, ptr)

                #lõpeta mäng nupp (all paremal)
                pygame.draw.rect(self.screen, (140, 50, 50), self.lopeta_rect)
                if (
                    self.raha >= self.lopeta_hind_raha
                    and self.parem_raha >= self.lopeta_hind_token
                ):
                    lop_s = "Lõpeta mäng"
                else:
                    lop_s = "..."
                lop_txt = self.font.render(lop_s, True, (255, 255, 255))
                self.screen.blit(lop_txt, lop_txt.get_rect(center=self.lopeta_rect.center))
                lop_hind = self.font.render(
                    f"{self.lopeta_hind_raha} € + {self.lopeta_hind_token} tokenit",
                    True,
                    (255, 255, 255),
                )
                self.screen.blit(
                    lop_hind,
                    lop_hind.get_rect(
                        midbottom=(self.lopeta_rect.centerx, self.lopeta_rect.top - 4)
                    ),
                )

            elif self.olek == "lõpp":
                #mängu lõpetamise tänileht
                self.screen.fill((25, 35, 50))
                t1 = self.font.render("Aitäh mängimast!", True, (255, 255, 255))
                t2 = self.font.render("Lõpetasid mängu.", True, (255, 255, 255))
                self.screen.blit(
                    t1, t1.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 30))
                )
                self.screen.blit(
                    t2, t2.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 20))
                )
                pygame.draw.rect(self.screen, (80, 80, 80), self.tagasi_rect)
                sulge = self.font.render("Sulge", True, (255, 255, 255))
                self.screen.blit(sulge, sulge.get_rect(center=self.tagasi_rect.center))

            elif self.olek == "upgrade":
                self.screen.fill((30, 30, 40))
                pealkiri = self.font.render("Täiustused", True, (255, 255, 255))
                self.screen.blit(pealkiri, pealkiri.get_rect(center=(SCREEN_WIDTH // 2, 120)))

                #upgrades olevad asjad
                raha_txt = self.font.render(f"Raha: {self.raha:.1f}", True, (255, 255, 255))
                self.screen.blit(raha_txt, (SCREEN_WIDTH - 200, 16))
                for i, info in enumerate(self.upgrade_info):
                    rea_r = self.upgrade_rea_rectid[i]
                    pygame.draw.rect(self.screen, (45, 48, 58), rea_r)
                    pygame.draw.rect(self.screen, (255, 220, 120), rea_r, width=3)

                    tx = rea_r.x + 16
                    ty = rea_r.y + 10
                    nimi = self.font.render(info["nimi"], True, (255, 255, 255))
                    self.screen.blit(nimi, (tx, ty))
                    kirj = self.font.render(info["kirjeldus"], True, (255, 255, 255))
                    self.screen.blit(kirj, (tx, ty + 28))
                    if info["tyyp"] == "klik":
                        hind = self.klik_jargmine_hind()
                        if self.upgrade_kliku_tase >= self.upgrade_kliku_max_tase:
                            nupu_s = "MAX"
                        elif self.raha >= hind:
                            nupu_s = "Osta"
                        else:
                            nupu_s = "..."
                        staatus_txt = (
                            f"Tase {self.upgrade_kliku_tase}/{self.upgrade_kliku_max_tase} · "
                            f"{self.raha_kliku:.1f} €/klõps · Hind: {hind}"
                        )
                    else:
                        hind = self.passiivne_jargmine_hind()
                        if self.passiivne_tase >= self.passiivne_max_tase:
                            nupu_s = "MAX"
                        elif self.raha >= hind:
                            nupu_s = "Osta"
                        else:
                            nupu_s = "..."
                        interv = self.passiivne_intervall_sek()
                        staatus_txt = (
                            f"Tase {self.passiivne_tase} · iga {interv:.1f} s +1 € · Hind: {hind}"
                        )
                    staatus = self.font.render(staatus_txt, True, (255, 255, 255))
                    self.screen.blit(staatus, (tx, ty + 52))

                    nupu_r = self.upgrade_nupu_rectid[i]
                    pygame.draw.rect(self.screen, (90, 70, 120), nupu_r)
                    nt = self.font.render(nupu_s, True, (255, 255, 255))
                    self.screen.blit(nt, nt.get_rect(center=nupu_r.center))


                pygame.draw.rect(self.screen, (80, 80, 80), self.tagasi_rect)
                tagasi_tekst = self.font.render("Tagasi", True, (255, 255, 255))
                self.screen.blit(
                    tagasi_tekst, tagasi_tekst.get_rect(center=self.tagasi_rect.center)
                )

            #pood ja selle sees olevad skinn ja taustapilt nupud
            elif self.olek == "pood":
                if self.pood_vaade == "valik":
                    pealkiri = self.font.render("Pood", True, (255, 255, 255))
                    pr = pealkiri.get_rect(center=(SCREEN_WIDTH // 2, 120))
                    self.screen.blit(pealkiri, pr)
                    pygame.draw.rect(self.screen, (70, 70, 120), self.pood_skinid_rect)
                    s1 = self.font.render("Skinnid", True, (255, 255, 255))
                    self.screen.blit(s1, s1.get_rect(center=self.pood_skinid_rect.center))
                    pygame.draw.rect(self.screen, (70, 120, 70), self.pood_taust_rect)
                    s2 = self.font.render("Taustapildid", True, (255, 255, 255))
                    self.screen.blit(s2, s2.get_rect(center=self.pood_taust_rect.center))
                    pygame.draw.rect(self.screen, (80, 80, 80), self.tagasi_rect)
                    tagasi_tekst = self.font.render("Tagasi", True, (255, 255, 255))
                    self.screen.blit(tagasi_tekst, tagasi_tekst.get_rect(center=self.tagasi_rect.center))

                elif self.pood_vaade == "skinnid":
                    pealkiri = self.font.render("Skinnid", True, (255, 255, 255))
                    self.screen.blit(pealkiri, pealkiri.get_rect(center=(SCREEN_WIDTH // 2, 56)))
                    raha_txt = self.font.render(f"Raha: {self.raha:.1f}", True, (255, 255, 255))
                    self.screen.blit(raha_txt, (SCREEN_WIDTH - 200, 16))
                    for i, info in enumerate(self.skinid_info):
                        y = 86 + i * 86
                        eelvaade = pygame.transform.scale(self.skin_pinnad[i], (72, 72))
                        self.screen.blit(eelvaade, (40, y))
                        nimi = self.font.render(info["nimi"], True, (255, 255, 255))
                        self.screen.blit(nimi, (130, y + 8))
                        hind_txt = self.font.render(f"Hind: {info['hind']}", True, (255, 255, 255))
                        self.screen.blit(hind_txt, (130, y + 38))
                        pygame.draw.rect(self.screen, (60, 60, 100), self.skin_nupu_rectid[i])
                        if i in self.ostetud_skinid or info["hind"] == 0:
                            nupu_s = "Vali"
                        elif self.raha >= info["hind"]:
                            nupu_s = "Osta"
                        else:
                            nupu_s = "..."
                        nt = self.font.render(nupu_s, True, (255, 255, 255))

                        self.screen.blit(nt, nt.get_rect(center=self.skin_nupu_rectid[i].center))
                    pygame.draw.rect(self.screen, (80, 80, 80), self.tagasi_rect)
                    tagasi_tekst = self.font.render("Tagasi", True, (255, 255, 255))
                    self.screen.blit(tagasi_tekst, tagasi_tekst.get_rect(center=self.tagasi_rect.center))



                elif self.pood_vaade == "taust":
                    pealkiri = self.font.render("Taustapildid", True, (255, 255, 255))
                    self.screen.blit(pealkiri, pealkiri.get_rect(center=(SCREEN_WIDTH // 2, 56)))
                    token_txt = self.font.render(f"Tokenid: {self.parem_raha}", True, (255, 255, 255))
                    self.screen.blit(token_txt, (SCREEN_WIDTH - 220, 16))
                    for i, info in enumerate(self.taustad_info):
                        y = 86 + i * 86
                        eelvaade = pygame.transform.scale(self.tausta_pinnad[i], (72, 72))
                        self.screen.blit(eelvaade, (40, y))
                        nimi = self.font.render(info["nimi"], True, (255, 255, 255))
                        self.screen.blit(nimi, (130, y + 8))
                        hind_txt = self.font.render(
                            f"Hind: {info['hind_token']} tokenit", True, (255, 255, 255)
                        )
                        self.screen.blit(hind_txt, (130, y + 38))
                        pygame.draw.rect(self.screen, (120, 70, 40), self.taust_nupu_rectid[i])
                        if i in self.ostetud_taustad or info["hind_token"] == 0:
                            nupu_s = "Vali"
                        elif self.parem_raha >= info["hind_token"]:
                            nupu_s = "Osta"
                        else:
                            nupu_s = "..."
                        nt = self.font.render(nupu_s, True, (255, 255, 255))
                        self.screen.blit(nt, nt.get_rect(center=self.taust_nupu_rectid[i].center))
                    pygame.draw.rect(self.screen, (80, 80, 80), self.tagasi_rect)
                    tagasi_tekst = self.font.render("Tagasi", True, (255, 255, 255))
                    self.screen.blit(tagasi_tekst, tagasi_tekst.get_rect(center=self.tagasi_rect.center))



            # Uuendab ekraani
            pygame.display.update()

        pygame.quit()
if __name__ == "__main__":
    Game().run()