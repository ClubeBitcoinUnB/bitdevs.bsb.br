---
layout: post
type: socratic
title: "Seminário Socrático 018"
meetup: https://www.meetup.com/brasilia-bitcoin/events/308443493/
---

## Avisos

* Entrem no grupo do Whatsapp "[BitdevsBSB](https://chat.whatsapp.com/KxuGyYu4TZy94KcA1yXCzi)" para ajudar na curadoria dos encontros!
* Siga Bitdevs Brasília no 
    * [Twitter](https://twitter.com/BitDevsBSB) e 
    * Nostr: npub1gttp04qscpuau2220hpave59dxtjj4put900gxw3y5jje7ugkzcqgml8r4

* Novos temas podem ser sugeridos nos [issues do GitHub do grupo](https://github.com/BitDevsBSB/BitDevsBSB/issues).
* Respeite a privacidade dos participantes.
* Os meetups nunca são gravados. Queremos todos a vontade para participar e discutir os assuntos programados, de forma anônima se assim o desejarem.
* [Livro - 101 Perguntas sobre Bitcoin](https://bitcoin101.site)
* [Clube Bitcoin UnB](https://x.com/ClubeBitcoinUnB)
* [Curso de Bitcoin do Edil](https://www.youtube.com/watch?v=gCgdCgyHFqw&list=PLfdR3_dt2rbexb-ohbaLLzAuNAp7Ypt8u)

## Agradecimentos

* Agradecemos à Vinteum por patrocinar as comidas e bebidas.

## Cronograma

### Aquecimento

* [Bitcoin for AI é sábado](https://bitcoinfor.ai)


### Bitcoin L1

* [Policy: uncap datacarrier by default (OP_RETURN drama ends?)](https://github.com/bitcoin/bitcoin/pull/32406)
  Bitcoin Core has merged PR #32406 which updates relay policy to:
  - uncap the OP_RETURN data size limit, previously set to 80 bytes
  - allow multiple OP_RETURN outputs in a single transaction
  - marks `-datacarrier` and `-datacarriersize` options as deprecated (but does not remove them)

  This change will be included in Bitcoin Core v30.  

* [Bitcoin Core development and transaction relay policy](https://bitcoincore.org/en/2025/06/06/relay-statement/)  
* [The Bitcoin Mempool: Private Mempools](https://bitcoinmagazine.com/technical/the-bitcoin-mempool-private-mempools)  
* [BTC mesh relay](https://x.com/eddieoz/status/1930339453417205908)
* [Block to roll out bitcoin payments on Square](https://block.xyz/inside/block-to-roll-out-bitcoin-payments-on-square)
* [ctv-csfs letter](https://ctv-csfs.com/)  
* [Broadcast own transactions only via short-lived Tor or I2P connections PR](https://github.com/bitcoin/bitcoin/pull/29415)  
  * [kdmukai summary](https://github.com/bitcoin/bitcoin/pull/29415#issuecomment-2956055221)
  * To improve privacy, broadcast locally submitted transactions (from the sendrawtransaction RPC) to the P2P network only via Tor or I2P short-lived connections, or to IPv4/IPv6 peers but through the Tor network.  

### L2

* [Bitlayer Partners with Miners to promote the adoption of BitVM](https://www.coindesk.com/business/2025/05/27/bitlayer-joins-forces-with-antpool-f2pool-and-spiderpool-to-supercharge-bitcoin-defi)  
* [BitVM on mainnet](https://x.com/robin_linus/status/1930291154022740005)
* [c= routing node is earning 9.7% APR on its bitcoin liquidity](https://x.com/RyanTheGentry/status/1927795177759928763)  
  * [c= website](https://cequals.xyz/)  

### Quantum Computing

* [Martin Habovštiak: Hashed keys are actually fully quantum secure](https://groups.google.com/g/bitcoindev/c/jr1QO95k6Uc)  
* [Jameson Lopp: Against Allowing Quantum Recovery of Bitcoin](https://groups.google.com/g/bitcoindev/c/uUK6py0Yjq0)  
* [Tadge Dryja: Post-Quantum commit / reveal Fawkescoin variant as a soft fork](https://groups.google.com/g/bitcoindev/c/LpWOcXMcvk8)  
* [Bitcoin-dev project: Bitcoin and Quantum Computing](https://x.com/Bitcoin_Devs/status/1929509963115667569)  
* [Bas Westerbaan: jpeg resistance of various post-quantum signature schemes](https://groups.google.com/g/bitcoindev/c/5Ff0jdQPofo)  

