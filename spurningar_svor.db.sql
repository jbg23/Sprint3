BEGIN TRANSACTION;
CREATE TABLE IF NOT EXISTS "Spurningar" (
	"SpID"	INT,
	"spurning"	TEXT,
	"rettSvar"	CHAR,
	"level"	INT,
	"mynd"	BLOB,
	PRIMARY KEY("SpID")
);
CREATE TABLE IF NOT EXISTS "Svor" (
	"SvID"	INT,
	"svor"	TEXT,
	"rettSvar"	CHAR,
	PRIMARY KEY("SvID")
);
INSERT INTO "Spurningar" VALUES (1,'Hvaða jólasveinn kemur fyrstur til byggða?','a',1,'');
INSERT INTO "Spurningar" VALUES (2,'Hvað heitir kærasti Mínu músar?','c',1,'');
INSERT INTO "Spurningar" VALUES (3,'Hvað heitir snjókarlinn í Frozen?','c',1,NULL);
INSERT INTO "Spurningar" VALUES (4,'Hvað heitir höfuðborg Danmerkur?','b',1,NULL);
INSERT INTO "Spurningar" VALUES (5,'Hvaða dýr er merki hjá verslunarkeðjunni Bónus?','d',1,NULL);
INSERT INTO "Spurningar" VALUES (6,'Í hvaða heimsálfu er Egyptaland?','b',1,NULL);
INSERT INTO "Spurningar" VALUES (7,'Hvað eru margar hliðar á trapissu?','b',1,NULL);
INSERT INTO "Spurningar" VALUES (8,'Hvað heitir asninn í Shrek?','a',1,NULL);
INSERT INTO "Spurningar" VALUES (9,'Hvernig eru buxurnar hans bangsímon á litinn?','d',1,NULL);
INSERT INTO "Spurningar" VALUES (10,'Hvenær er þjóðhátíðardagur Íslendinga?','c',1,NULL);
INSERT INTO "Svor" VALUES (1,'(a) Stekkjastaur
(b) Stúfur
(c) Giljagaur
(d) Kertasníkir','a');
INSERT INTO "Svor" VALUES (2,'(a) Mikki refur
(b) Jenni
(c) Mikki mús
(d) Stuart litli','c');
INSERT INTO "Svor" VALUES (3,'(a) Guðmundur
(b) Ingólfur
(c) Ólafur
(d) Snæfinnur','c');
INSERT INTO "Svor" VALUES (4,'(a) Árhús
(b) Kaupmannahöfn
(c) Stokkhólmur
(d) Álaborg','b');
INSERT INTO "Svor" VALUES (5,'(a) Köttur
(b) Mús
(c) Villisvín
(d) Grís','d');
INSERT INTO "Svor" VALUES (6,'(a) Evrópa
(b) Afríka
(c) Asía
(d) Eyjaálfa','b');
INSERT INTO "Svor" VALUES (7,'(a) Fimm
(b) Fjórar
(c) Þrjár
(d) Núll','b');
INSERT INTO "Svor" VALUES (8,'(a) Asni
(b) Eyrnaslapi
(c) Fáviti
(d) Fíóna','a');
INSERT INTO "Svor" VALUES (9,'(a) Rauðar
(b) Bláar
(c) Grænar
(d) Hann er ekki í buxum','d');
INSERT INTO "Svor" VALUES (10,'(a) Fyrsta sunnudag í ágúst
(b) 1.maí
(c) 17.júní
(d) 4.júlí','c');
COMMIT;
