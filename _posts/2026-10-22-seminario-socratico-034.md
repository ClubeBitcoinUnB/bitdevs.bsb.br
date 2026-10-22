---
layout: post
type: socratic
title: "Seminário Socrático 034"
meetup: https://app.evento.so/e/evt_hY6BhUSvT7zbsZ1b
---

## Avisos

* Respeite a privacidade dos participantes.
* Os meetups nunca são gravados. Queremos todos à vontade para participar e discutir os assuntos programados, de forma anônima se assim o desejarem.
* Perguntas básicas e contrapontos técnicos são bem-vindos.
* Novos temas podem ser sugeridos nos [issues do GitHub](https://github.com/ClubeBitcoinUnB/bitdevs.bsb.br/issues).

## Cronograma

### Aquecimento

* [Ghostly 1.0: mensageiro P2P com pagamentos em sats, apresentado por Miguel Medeiros](https://x.com/_miguelmedeiros/status/2106013581422497934)
    * [Código MIT: carteiras integradas e uso em mainnet experimental](https://github.com/MiguelMedeiros/ghostly)
    * [Especificações abertas dos protocolos (WISPs)](https://ghostly.tools/wisps)

### Bitcoin L1

* [Bitcoin Core 32.0rc4: candidato de lançamento disponível para testes](https://bitcoincore.org/bin/bitcoin-core-32.0/test.rc4/)
    * [Guia oficial de testes do release candidate](https://github.com/bitcoin-core/bitcoin-devwiki/wiki/32.0-Release-Candidate-Testing-Guide)
* [Privacidade de origem: completar as três conexões de private broadcast (Core #36277)](https://github.com/bitcoin/bitcoin/pull/36277)
    * [Optech: correção contra ataques de timing na transmissão privada](https://bitcoinops.org/en/newsletters/2026/10/09/#bitcoin-core-36277)
* [BIP324: proposta de aliases dinâmicos para mensagens P2P](https://groups.google.com/g/bitcoindev/c/YjrkzS_Sjes)
    * [Draft BIP #2301: negociação de identificadores curtos para novas mensagens](https://github.com/bitcoin/bips/pull/2301)
    * [Optech: funcionamento e limites dos aliases dinâmicos](https://bitcoinops.org/en/newsletters/2026/10/09/#dynamic-one-byte-message-type-ids-for-bip324)
* [Silent Payments: correção da extração de chave pública em scriptSig P2PKH maleado (Core #36338)](https://github.com/bitcoin/bitcoin/pull/36338)
    * [Optech: falha poderia fazer o scanner perder pagamentos; implementação ainda não integrada à carteira](https://bitcoinops.org/en/newsletters/2026/10/09/#bitcoin-core-36338)
    * [BIP375 em draft: envio de Silent Payments com PSBTv2 e provas DLEQ](https://github.com/bitcoin/bips/blob/master/bip-0375.mediawiki)
* [BIP54: limites de crescimento da cadeia com as duas correções de timewarp, com prova em Lean](https://delvingbitcoin.org/t/bounds-on-chain-length-with-bip-54-timewarp-fixes/2899)
* [BIP110, com status Closed: proposta de restrições temporárias de consenso para dados e scripts](https://github.com/bitcoin/bips/blob/master/bip-0110.mediawiki)

### Lightning e L2

* [LDK 0.2.7: correções de segurança em reconexão, LSPS2 e DoS](https://github.com/lightningdevkit/rust-lightning/releases/tag/v0.2.7)
    * [LDK 0.1.13: correções de segurança para a série 0.1](https://github.com/lightningdevkit/rust-lightning/releases/tag/v0.1.13)
* [LDK 0.3-rc3: RBF para splices, entrada e saída de fundos no mesmo splice e anchors por padrão](https://github.com/lightningdevkit/rust-lightning/releases/tag/v0.3-rc3)
* [Core Lightning 26.06.9: correções de segurança e de regressão no gossip](https://github.com/ElementsProject/lightning/releases/tag/v26.06.9)
    * [Relato de bug: splice_update não retorna, mesmo após desconectar o peer (CLN #9599)](https://github.com/ElementsProject/lightning/issues/9599)
* [Eclair: dois DoS na abertura de canais, corrigidos em 0.14.1](https://delvingbitcoin.org/t/disclosure-dos-vulnerabilities-fixed-in-eclair-v0-14-1/2928)
    * [Outro disclosure: DoS em feature parsing e descompressão de gossip, corrigidos em 0.14.0](https://bitcoinops.org/en/newsletters/2026/10/02/#disclosure-of-two-dos-vulnerabilities-in-eclair)
* [LN-GAP: proposta de contratos de múltiplas rodadas em canais Lightning, com comitê de atestação](https://github.com/AdamISZ/ln-gap)
    * [Discussão original de Adam Gibson: jogos e provas de armazenamento como exemplos](https://groups.google.com/g/bitcoindev/c/pjv6bL_42kg)
    * [Optech #427: comitê não custodia fundos, mas a segurança depende de maioria honesta](https://bitcoinops.org/en/newsletters/2026/10/16/)
* [Cashu federado: emissão cega BLS, consenso AlephBFT e reservas com FROST — experimento de Calle](https://github.com/callebtc/federated-cashu/blob/main/slides/federated-cashu/speaker-notes.ts)
* [Nutroot: proposta de condições de gasto para Cashu inspiradas em Taproot (NUTs #443)](https://github.com/cashubtc/nuts/pull/443)
* [nonfungible.cash: imagens como portadoras de credenciais — criptografia experimental e não auditada](https://nonfungible.cash/)
    * [Credenciais Pointcheval–Sanders sobre BLS12-381 nos metadados do arquivo](https://nonfungible.cash/how-it-works?view=cryptography)
    * [Transferência: resgate no mint e consumo do nullifier; copiar o arquivo não garante exclusividade](https://nonfungible.cash/how-it-works?view=cryptography#send)
    * [Modo de exibição sem entregar a credencial de gasto](https://nonfungible.cash/how-it-works?view=cryptography#show)
    * [Modelo de confiança: emissão excessiva, recusa de serviço e JavaScript do mint](https://nonfungible.cash/how-it-works?view=cryptography#trust)
* [LayerTree: saída unilateral em uma transação de um UTXO compartilhado](https://x.com/roasbeef/status/2110813488822239619)
    * [Implementação de referência da Lightning Labs](https://github.com/lightninglabs/layertree)
    * [Especificação em draft: árvore Merkle-sum, provas de saída e contenção pelo UTXO](https://github.com/lightninglabs/layertree/blob/f6c4d296130fa39f32d383eb841c82f9ea575539/spec/layertree.md)
    * [Hipóteses e limites: depende de mudanças de consenso ainda não ativadas; uma transação não implica custo ou latência constantes](https://github.com/lightninglabs/layertree/blob/f6c4d296130fa39f32d383eb841c82f9ea575539/CONCEPTS.md)

### Nostr

* [Armada Stack: hospedagem própria de comunidades Nostr com cliente, relay, mídia cifrada e chamadas](https://soapbox.pub/blog/how-to-self-host-armada)
    * [Protocolos de comunidades e modelo de implantação do Armada](https://soapbox.pub/armada)
* [NIP-78: debate sobre AUTH e acesso aos dados de aplicações — privacidade por padrão e compatibilidade](https://github.com/nostr-protocol/nips/issues/2473)
* [Draft NIP-FB/NIP-FE: envelopes para múltiplos destinatários e feeds privados](https://github.com/nostr-protocol/nips/pull/2488)

### Criptografia, privacidade e segurança

* [Claude e o mistério das curvas NIST: origem das seeds públicas reconstruída com lrand48 e timestamps](https://www.anthropic.com/research/ecdsa-curve-origins)
    * [Resultado esclarece a escolha de parâmetros; não demonstra quebra de ECDSA nem recuperação de chaves privadas](https://www.anthropic.com/research/ecdsa-curve-origins#what-this-means)
* [Shielded Bitcoin: metaprotocolo de transferências privadas e suas hipóteses de segurança](https://delvingbitcoin.org/t/shielded-bitcoin-private-transfers-on-the-bitcoin-l1/2912)
    * [Optech: provas fora do consenso Bitcoin e questões de entrada e saída](https://bitcoinops.org/en/newsletters/2026/10/09/#proposal-for-onchain-private-bitcoin-transfers-with-no-consensus-changes)
    * [Paper de Clara Shikhelman, Mikhail Komarov e Aleksei Moskvin](https://www.allocinit.xyz/uploads/shielded-bitcoin.pdf)
* [Convenções de tagged hashes nos BIPs: número do BIP, separação de domínio e compatibilidade](https://groups.google.com/g/bitcoindev/c/VQVNZOR3-kg)
* [Proposta de agregação de assinaturas pós-quânticas de um bloco via SNARKs: custos e hipóteses](https://delvingbitcoin.org/t/block-wide-signature-aggregation-via-snarks/2875)
    * [Continuação do debate sobre tipos de outputs pós-quânticos, P2TRv2 e P2MR](https://delvingbitcoin.org/t/pqc-output-type-discussion/2749/18)
    * [Dan Boneh no Bitcoin Rails #61: caminhos para uma transição pós-quântica](https://youtu.be/F-HG87VJj_k)
* [Compact Shielded CSV: proposta de blockchain própria com validação no cliente e criptografia pós-quântica](https://arxiv.org/abs/2609.32015)
    * [Paper: nullifier, degriefer e compromisso da transação; três hashes por transação de uma entrada, com provas fora da cadeia](https://arxiv.org/pdf/2609.32015)
* [Ledger: implantes físicos em dispositivos de revendedores para capturar a frase de recuperação durante a configuração](https://www.ledger.com/blog-response-hardware-implant-attack)
* [PwnEscape (CVE-2026-99999): metadados de checksum IPv4 e escape de máquina virtual para o host](https://www.pwn.ai/blog/pwnescape)
    * [Aviso da Red Hat: impacto no kernel Linux e versões afetadas](https://access.redhat.com/security/cve/cve-2026-99999)
