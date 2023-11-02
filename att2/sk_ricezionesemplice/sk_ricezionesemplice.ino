/*il programma deve stare in ascolto sul pin digitale, dall'analisi con il pycoscope si vede 
un'onda quadra tra 0 e 5v in cui ogni bit ha 833 microsecondi di vita. Il primo bit è il
bit di start ed è a 0, prima di questo esce sempre 1. Appena si legge 0 inizia il procedimento
di lettura. 
L'intenzione è piazzarsi più o meno a metà bit, per ottenere ciò la prima volta si saltano 
833 + 416 microsecondi (833 per il bit di start e i restanti 416 per piazzarsi più o meno
a metà del secondo bit, poi si salta ogni volta di 833 microsecondi fino a termine lettura.
unico difetto di lettura è il fatto che si legge al contrario perciò il pacchetto va capovolto*/

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  pinMode(7,INPUT); // di solito si impostava il pin digitale in output ma ora deve stare
                    // in ascolto
}

void loop() {
  // put your main code here, to run repeatedly:
  unsigned int b[8]; // array in cui salvare i bit quando li legge
  unsigned int t=0;  // valore temporaneo per il primo bit
  unsigned int c=0;  // contatore per i cicli

  t=digitalRead(7);
  if(t==0){     //appena becca il valore 0 parte la lettura
    delayMicroseconds(1249);  // 833*416
    for(c=0;c<8;c++){    // ciclo per riempire l'array
      b[c]=digitalRead(7);
      delayMicroseconds(833);
    }
    for(c=0;c<4;c++){    // ciclo per l'inversione dell'array
      b[c]=b[c]+b[7-c];
      b[7-c]=b[c]-b[7-c];
      b[c]=b[c]-b[7-c];
    }
    Serial.println("----");
    Serial.println(97);
    for(c=0;c<8;c++){    // per stampare il risultato 
      Serial.print(b[c]);
    }
  }
}
