Questa è il menù in cui troverete i report sulle chiamate fatte e ricevute dal vostro CloudPBX, di seguito una breve descrizione dei vari sotto menù:

- [Call Detail](#call-detail)
- [Date Hour Wise Call](#date-hour-wise-call)
- [Estension Calls Summary](#estension-calls-summary)

  

## Call Detail

In questo sotto menù poterete avere un recap di ogni singola chiamata arrivata o effettuata dalle vostre extension, oltre ai dati temporali e puramente indicativi dell'instradamento della chiamata, se espandete ogni singola entry della tabella cliccando sul pulsante ![](./attachments/image2019-6-4_16-20-50.png)

, avrete accesso ad ulteriori informazioni sull'andamento della chiamata:

![](./attachments/image2019-6-4_16-21-42.png)

In particolare vi verranno mostrati dei parametri fondamentali che riguardano la qualità dell'audio durante la conversazione. In particolare dovete stare attenti a questi parametri:

1. **Jitter Maximum Variance:** questo parametro sta ad indicare la massima variazione di **Jitter** durante la chiamata, questo valore deve essere il più basso possibile, un Jitter buono dovrebbe rimanere tra il valore 0 e il valore 60.

> [!INFO]
> Il ***Jitter*** è l’intero intervallo di tempo per gestire la sequenza dei pacchetti RTP in arrivo. Se i pacchetti RTP arrivano a intervalli regolari e nella sequenza corretta, allora siamo nel caso di un Jitter basso. Se arrivano frammentati o se con una sequenza non corretta, allora abbiamo un valore di Jitter elevato. Il Jitter si crea quando il flusso di pacchetti RTP attraversa la rete LAN, WAN o Internet insieme ad altri dati condivisi sulla stessa di rete.

1. **Quality Percentage:** questa percentuale indica il Packet-Loss registrato dal CloudPBX durante la chiamata. Se questo valore è una percentuale per cui il valore 100 indica nessun packet-loss.
2. **MOS:** il MOS (acronimo di **Mean Opinion Score**), è un indice che, attraverso la combinazione di alcuni parametri di qualità dell'audio (come quelli indicati sopra), ci può dare un indicazione di quanto può essere stata soddisfacente la qualità dell'audio durante una chiamata,![](./attachments/image2019-6-4_16-34-43.png)

  

## Date Hour Wise Call

In questo sotto -menù potete vedere un report della quantità di chiamate effettuate/ricevute giornalmente e suddivise nelle 24 ore giornaliere.

## Estension Calls Summary

In questo sotto-menù potrete vedere un report delle chiamate effettuate / ricevute da ogni singola extension del vostro CloudPBX.