{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "seeing-action",
   "metadata": {},
   "outputs": [],
   "source": [
    "text = \"\"\"\n",
    "A stock exchange is an exchange (or bourse)[note 1] where stockbrokers and traders can buy and sell shares (equity stock), bonds, and other securities. Many large companies have their stocks listed on a stock exchange. This makes the stock more liquid and thus more attractive to many investors. The exchange may also act as a guarantor of settlement. These and other stocks may also be traded \"over the counter\" (OTC), that is, through a dealer. Some large companies will have their stock listed on more than one exchange in different countries, so as to attract international investors.[6]\n",
    "\n",
    "Stock exchanges may also cover other types of securities, such as fixed-interest securities (bonds) or (less frequently) derivatives, which are more likely to be traded OTC.\n",
    "\n",
    "Trade in stock markets means the transfer (in exchange for money) of a stock or security from a seller to a buyer. This requires these two parties to agree on a price. Equities (stocks or shares) confer an ownership interest in a particular company.\n",
    "\n",
    "Participants in the stock market range from small individual stock investors to larger investors, who can be based anywhere in the world, and may include banks, insurance companies, pension funds and hedge funds. Their buy or sell orders may be executed on their behalf by a stock exchange trader.\n",
    "\n",
    "Some exchanges are physical locations where transactions are carried out on a trading floor, by a method known as open outcry. This method is used in some stock exchanges and commodities exchanges, and involves traders shouting bid and offer prices. The other type of stock exchange has a network of computers where trades are made electronically. An example of such an exchange is the NASDAQ.\n",
    "\n",
    "A potential buyer bids a specific price for a stock, and a potential seller asks a specific price for the same stock. Buying or selling at the Market means you will accept any ask price or bid price for the stock. When the bid and ask prices match, a sale takes place, on a first-come, first-served basis if there are multiple bidders at a given price.\n",
    "\n",
    "The purpose of a stock exchange is to facilitate the exchange of securities between buyers and sellers, thus providing a marketplace. The exchanges provide real-time trading information on the listed securities, facilitating price discovery.\n",
    "\n",
    "The New York Stock Exchange (NYSE) is a physical exchange, with a hybrid market for placing orders electronically from any location as well as on the trading floor. Orders executed on the trading floor enter by way of exchange members and flow down to a floor broker, who submits the order electronically to the floor trading post for the Designated market maker (\"DMM\") for that stock to trade the order. The DMM's job is to maintain a two-sided market, making orders to buy and sell the security when there are no other buyers or sellers. If a bid–ask spread exists, no trade immediately takes place – in this case the DMM may use their own resources (money or stock) to close the difference. Once a trade has been made, the details are reported on the \"tape\" and sent back to the brokerage firm, which then notifies the investor who placed the order. Computers play an important role, especially for program trading.\n",
    "\n",
    "The NASDAQ is an electronic exchange, where all of the trading is done over a computer network. The process is similar to the New York Stock Exchange. One or more NASDAQ market makers will always provide a bid and ask the price at which they will always purchase or sell 'their' stock.\n",
    "\n",
    "The Paris Bourse, now part of Euronext, is an order-driven, electronic stock exchange. It was automated in the late 1980s. Prior to the 1980s, it consisted of an open outcry exchange. Stockbrokers met on the trading floor of the Palais Brongniart. In 1986, the CATS trading system was introduced, and the order matching system was fully automated.\n",
    "\n",
    "People trading stock will prefer to trade on the most popular exchange since this gives the largest number of potential counter parties (buyers for a seller, sellers for a buyer) and probably the best price. However, there have always been alternatives such as brokers trying to bring parties together to trade outside the exchange. Some third markets that were popular are Instinet, and later Island and Archipelago (the latter two have since been acquired by Nasdaq and NYSE, respectively). One advantage is that this avoids the commissions of the exchange. However, it also has problems such as adverse selection.[7] Financial regulators have probed dark pools.[8][9]\n",
    "\n",
    "\"\"\""
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "circular-score",
   "metadata": {},
   "outputs": [],
   "source": [
    "import spacy \n",
    "from spacy.lang.en.stop_words import STOP_WORDS\n",
    "from string import punctuation"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "prime-competition",
   "metadata": {},
   "outputs": [],
   "source": [
    "stopwords = list(STOP_WORDS)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "broke-retailer",
   "metadata": {},
   "outputs": [],
   "source": [
    "nlp = spacy.load('en_core_web_sm')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "heavy-expert",
   "metadata": {},
   "outputs": [],
   "source": [
    "doc = nlp(text)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "enormous-kitchen",
   "metadata": {},
   "outputs": [],
   "source": [
    "tokens = [token.text for token in doc]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 50,
   "id": "judicial-assistant",
   "metadata": {},
   "outputs": [],
   "source": [
    "punctuation = punctuation + '\\n'"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 51,
   "id": "suspended-handbook",
   "metadata": {},
   "outputs": [],
   "source": [
    "word_frequencies = {}\n",
    "for word in doc:\n",
    "    if word.text.lower() not in stopwords:\n",
    "        if word.text.lower() not in punctuation:\n",
    "            if word.text not in word_frequencies.keys():\n",
    "                word_frequencies[word.text] = 1\n",
    "            else:\n",
    "                word_frequencies[word.text] += 1"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 52,
   "id": "changed-analyst",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{'stock': 21, 'exchange': 19, 'bourse)[note': 1, '1': 1, 'stockbrokers': 1, 'traders': 2, 'buy': 3, 'sell': 4, 'shares': 2, 'equity': 1, 'bonds': 2, 'securities': 5, 'large': 2, 'companies': 3, 'stocks': 3, 'listed': 3, 'makes': 1, 'liquid': 1, 'attractive': 1, 'investors': 3, 'act': 1, 'guarantor': 1, 'settlement': 1, 'traded': 2, 'counter': 2, 'OTC': 2, 'dealer': 1, 'different': 1, 'countries': 1, 'attract': 1, 'international': 1, 'investors.[6': 1, 'Stock': 3, 'exchanges': 5, 'cover': 1, 'types': 1, 'fixed': 1, 'interest': 2, 'frequently': 1, 'derivatives': 1, 'likely': 1, 'Trade': 1, 'markets': 2, 'means': 2, 'transfer': 1, 'money': 2, 'security': 2, 'seller': 3, 'buyer': 3, 'requires': 1, 'parties': 3, 'agree': 1, 'price': 9, 'Equities': 1, 'confer': 1, 'ownership': 1, 'particular': 1, 'company': 1, 'Participants': 1, 'market': 5, 'range': 1, 'small': 1, 'individual': 1, 'larger': 1, 'based': 1, 'world': 1, 'include': 1, 'banks': 1, 'insurance': 1, 'pension': 1, 'funds': 2, 'hedge': 1, 'orders': 3, 'executed': 2, 'behalf': 1, 'trader': 1, 'physical': 2, 'locations': 1, 'transactions': 1, 'carried': 1, 'trading': 10, 'floor': 6, 'method': 2, 'known': 1, 'open': 2, 'outcry': 2, 'commodities': 1, 'involves': 1, 'shouting': 1, 'bid': 5, 'offer': 1, 'prices': 2, 'type': 1, 'network': 2, 'computers': 1, 'trades': 1, 'electronically': 3, 'example': 1, 'NASDAQ': 3, 'potential': 3, 'bids': 1, 'specific': 2, 'asks': 1, 'Buying': 1, 'selling': 1, 'Market': 1, 'accept': 1, 'ask': 4, 'match': 1, 'sale': 1, 'takes': 2, 'place': 2, 'come': 1, 'served': 1, 'basis': 1, 'multiple': 1, 'bidders': 1, 'given': 1, 'purpose': 1, 'facilitate': 1, 'buyers': 3, 'sellers': 3, 'providing': 1, 'marketplace': 1, 'provide': 2, 'real': 1, 'time': 1, 'information': 1, 'facilitating': 1, 'discovery': 1, 'New': 2, 'York': 2, 'Exchange': 2, 'NYSE': 2, 'hybrid': 1, 'placing': 1, 'location': 1, 'Orders': 1, 'enter': 1, 'way': 1, 'members': 1, 'flow': 1, 'broker': 1, 'submits': 1, 'order': 5, 'post': 1, 'Designated': 1, 'maker': 1, 'DMM': 3, 'trade': 5, 'job': 1, 'maintain': 1, 'sided': 1, 'making': 1, '–': 2, 'spread': 1, 'exists': 1, 'immediately': 1, 'case': 1, 'use': 1, 'resources': 1, 'close': 1, 'difference': 1, 'details': 1, 'reported': 1, 'tape': 1, 'sent': 1, 'brokerage': 1, 'firm': 1, 'notifies': 1, 'investor': 1, 'placed': 1, 'Computers': 1, 'play': 1, 'important': 1, 'role': 1, 'especially': 1, 'program': 1, 'electronic': 2, 'computer': 1, 'process': 1, 'similar': 1, 'makers': 1, 'purchase': 1, 'Paris': 1, 'Bourse': 1, 'Euronext': 1, 'driven': 1, 'automated': 2, 'late': 1, '1980s': 2, 'Prior': 1, 'consisted': 1, 'Stockbrokers': 1, 'met': 1, 'Palais': 1, 'Brongniart': 1, '1986': 1, 'CATS': 1, 'system': 2, 'introduced': 1, 'matching': 1, 'fully': 1, 'People': 1, 'prefer': 1, 'popular': 2, 'gives': 1, 'largest': 1, 'number': 1, 'probably': 1, 'best': 1, 'alternatives': 1, 'brokers': 1, 'trying': 1, 'bring': 1, 'outside': 1, 'Instinet': 1, 'later': 1, 'Island': 1, 'Archipelago': 1, 'acquired': 1, 'Nasdaq': 1, 'respectively': 1, 'advantage': 1, 'avoids': 1, 'commissions': 1, 'problems': 1, 'adverse': 1, 'selection.[7': 1, 'Financial': 1, 'regulators': 1, 'probed': 1, 'dark': 1, 'pools.[8][9': 1}\n"
     ]
    }
   ],
   "source": [
    "print(word_frequencies)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 53,
   "id": "alternate-level",
   "metadata": {},
   "outputs": [],
   "source": [
    "max_frequency = max(word_frequencies.values())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 54,
   "id": "aging-snapshot",
   "metadata": {},
   "outputs": [],
   "source": [
    "for word in word_frequencies.keys():\n",
    "    word_frequencies[word] = word_frequencies[word]/max_frequency"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 55,
   "id": "another-junior",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{'stock': 1.0, 'exchange': 0.9047619047619048, 'bourse)[note': 0.047619047619047616, '1': 0.047619047619047616, 'stockbrokers': 0.047619047619047616, 'traders': 0.09523809523809523, 'buy': 0.14285714285714285, 'sell': 0.19047619047619047, 'shares': 0.09523809523809523, 'equity': 0.047619047619047616, 'bonds': 0.09523809523809523, 'securities': 0.23809523809523808, 'large': 0.09523809523809523, 'companies': 0.14285714285714285, 'stocks': 0.14285714285714285, 'listed': 0.14285714285714285, 'makes': 0.047619047619047616, 'liquid': 0.047619047619047616, 'attractive': 0.047619047619047616, 'investors': 0.14285714285714285, 'act': 0.047619047619047616, 'guarantor': 0.047619047619047616, 'settlement': 0.047619047619047616, 'traded': 0.09523809523809523, 'counter': 0.09523809523809523, 'OTC': 0.09523809523809523, 'dealer': 0.047619047619047616, 'different': 0.047619047619047616, 'countries': 0.047619047619047616, 'attract': 0.047619047619047616, 'international': 0.047619047619047616, 'investors.[6': 0.047619047619047616, 'Stock': 0.14285714285714285, 'exchanges': 0.23809523809523808, 'cover': 0.047619047619047616, 'types': 0.047619047619047616, 'fixed': 0.047619047619047616, 'interest': 0.09523809523809523, 'frequently': 0.047619047619047616, 'derivatives': 0.047619047619047616, 'likely': 0.047619047619047616, 'Trade': 0.047619047619047616, 'markets': 0.09523809523809523, 'means': 0.09523809523809523, 'transfer': 0.047619047619047616, 'money': 0.09523809523809523, 'security': 0.09523809523809523, 'seller': 0.14285714285714285, 'buyer': 0.14285714285714285, 'requires': 0.047619047619047616, 'parties': 0.14285714285714285, 'agree': 0.047619047619047616, 'price': 0.42857142857142855, 'Equities': 0.047619047619047616, 'confer': 0.047619047619047616, 'ownership': 0.047619047619047616, 'particular': 0.047619047619047616, 'company': 0.047619047619047616, 'Participants': 0.047619047619047616, 'market': 0.23809523809523808, 'range': 0.047619047619047616, 'small': 0.047619047619047616, 'individual': 0.047619047619047616, 'larger': 0.047619047619047616, 'based': 0.047619047619047616, 'world': 0.047619047619047616, 'include': 0.047619047619047616, 'banks': 0.047619047619047616, 'insurance': 0.047619047619047616, 'pension': 0.047619047619047616, 'funds': 0.09523809523809523, 'hedge': 0.047619047619047616, 'orders': 0.14285714285714285, 'executed': 0.09523809523809523, 'behalf': 0.047619047619047616, 'trader': 0.047619047619047616, 'physical': 0.09523809523809523, 'locations': 0.047619047619047616, 'transactions': 0.047619047619047616, 'carried': 0.047619047619047616, 'trading': 0.47619047619047616, 'floor': 0.2857142857142857, 'method': 0.09523809523809523, 'known': 0.047619047619047616, 'open': 0.09523809523809523, 'outcry': 0.09523809523809523, 'commodities': 0.047619047619047616, 'involves': 0.047619047619047616, 'shouting': 0.047619047619047616, 'bid': 0.23809523809523808, 'offer': 0.047619047619047616, 'prices': 0.09523809523809523, 'type': 0.047619047619047616, 'network': 0.09523809523809523, 'computers': 0.047619047619047616, 'trades': 0.047619047619047616, 'electronically': 0.14285714285714285, 'example': 0.047619047619047616, 'NASDAQ': 0.14285714285714285, 'potential': 0.14285714285714285, 'bids': 0.047619047619047616, 'specific': 0.09523809523809523, 'asks': 0.047619047619047616, 'Buying': 0.047619047619047616, 'selling': 0.047619047619047616, 'Market': 0.047619047619047616, 'accept': 0.047619047619047616, 'ask': 0.19047619047619047, 'match': 0.047619047619047616, 'sale': 0.047619047619047616, 'takes': 0.09523809523809523, 'place': 0.09523809523809523, 'come': 0.047619047619047616, 'served': 0.047619047619047616, 'basis': 0.047619047619047616, 'multiple': 0.047619047619047616, 'bidders': 0.047619047619047616, 'given': 0.047619047619047616, 'purpose': 0.047619047619047616, 'facilitate': 0.047619047619047616, 'buyers': 0.14285714285714285, 'sellers': 0.14285714285714285, 'providing': 0.047619047619047616, 'marketplace': 0.047619047619047616, 'provide': 0.09523809523809523, 'real': 0.047619047619047616, 'time': 0.047619047619047616, 'information': 0.047619047619047616, 'facilitating': 0.047619047619047616, 'discovery': 0.047619047619047616, 'New': 0.09523809523809523, 'York': 0.09523809523809523, 'Exchange': 0.09523809523809523, 'NYSE': 0.09523809523809523, 'hybrid': 0.047619047619047616, 'placing': 0.047619047619047616, 'location': 0.047619047619047616, 'Orders': 0.047619047619047616, 'enter': 0.047619047619047616, 'way': 0.047619047619047616, 'members': 0.047619047619047616, 'flow': 0.047619047619047616, 'broker': 0.047619047619047616, 'submits': 0.047619047619047616, 'order': 0.23809523809523808, 'post': 0.047619047619047616, 'Designated': 0.047619047619047616, 'maker': 0.047619047619047616, 'DMM': 0.14285714285714285, 'trade': 0.23809523809523808, 'job': 0.047619047619047616, 'maintain': 0.047619047619047616, 'sided': 0.047619047619047616, 'making': 0.047619047619047616, '–': 0.09523809523809523, 'spread': 0.047619047619047616, 'exists': 0.047619047619047616, 'immediately': 0.047619047619047616, 'case': 0.047619047619047616, 'use': 0.047619047619047616, 'resources': 0.047619047619047616, 'close': 0.047619047619047616, 'difference': 0.047619047619047616, 'details': 0.047619047619047616, 'reported': 0.047619047619047616, 'tape': 0.047619047619047616, 'sent': 0.047619047619047616, 'brokerage': 0.047619047619047616, 'firm': 0.047619047619047616, 'notifies': 0.047619047619047616, 'investor': 0.047619047619047616, 'placed': 0.047619047619047616, 'Computers': 0.047619047619047616, 'play': 0.047619047619047616, 'important': 0.047619047619047616, 'role': 0.047619047619047616, 'especially': 0.047619047619047616, 'program': 0.047619047619047616, 'electronic': 0.09523809523809523, 'computer': 0.047619047619047616, 'process': 0.047619047619047616, 'similar': 0.047619047619047616, 'makers': 0.047619047619047616, 'purchase': 0.047619047619047616, 'Paris': 0.047619047619047616, 'Bourse': 0.047619047619047616, 'Euronext': 0.047619047619047616, 'driven': 0.047619047619047616, 'automated': 0.09523809523809523, 'late': 0.047619047619047616, '1980s': 0.09523809523809523, 'Prior': 0.047619047619047616, 'consisted': 0.047619047619047616, 'Stockbrokers': 0.047619047619047616, 'met': 0.047619047619047616, 'Palais': 0.047619047619047616, 'Brongniart': 0.047619047619047616, '1986': 0.047619047619047616, 'CATS': 0.047619047619047616, 'system': 0.09523809523809523, 'introduced': 0.047619047619047616, 'matching': 0.047619047619047616, 'fully': 0.047619047619047616, 'People': 0.047619047619047616, 'prefer': 0.047619047619047616, 'popular': 0.09523809523809523, 'gives': 0.047619047619047616, 'largest': 0.047619047619047616, 'number': 0.047619047619047616, 'probably': 0.047619047619047616, 'best': 0.047619047619047616, 'alternatives': 0.047619047619047616, 'brokers': 0.047619047619047616, 'trying': 0.047619047619047616, 'bring': 0.047619047619047616, 'outside': 0.047619047619047616, 'Instinet': 0.047619047619047616, 'later': 0.047619047619047616, 'Island': 0.047619047619047616, 'Archipelago': 0.047619047619047616, 'acquired': 0.047619047619047616, 'Nasdaq': 0.047619047619047616, 'respectively': 0.047619047619047616, 'advantage': 0.047619047619047616, 'avoids': 0.047619047619047616, 'commissions': 0.047619047619047616, 'problems': 0.047619047619047616, 'adverse': 0.047619047619047616, 'selection.[7': 0.047619047619047616, 'Financial': 0.047619047619047616, 'regulators': 0.047619047619047616, 'probed': 0.047619047619047616, 'dark': 0.047619047619047616, 'pools.[8][9': 0.047619047619047616}\n"
     ]
    }
   ],
   "source": [
    "print(word_frequencies)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 56,
   "id": "commercial-paper",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[\n",
      ", A stock exchange is an exchange (or bourse)[note 1] where stockbrokers and traders can buy and sell shares (equity stock), bonds, and other securities., Many large companies have their stocks listed on a stock exchange., This makes the stock more liquid and thus more attractive to many investors., The exchange may also act as a guarantor of settlement., These and other stocks may also be traded \"over the counter\" (OTC), that is, through a dealer., Some large companies will have their stock listed on more than one exchange in different countries, so as to attract international investors.[6]\n",
      "\n",
      "Stock exchanges may also cover other types of securities, such as fixed-interest securities (bonds) or (less frequently) derivatives, which are more likely to be traded OTC., \n",
      "\n",
      "Trade in stock markets means the transfer (in exchange for money) of a stock or security from a seller to a buyer., This requires these two parties to agree on a price., Equities (stocks or shares) confer an ownership interest in a particular company., \n",
      "\n",
      "Participants in the stock market range from small individual stock investors to larger investors, who can be based anywhere in the world, and may include banks, insurance companies, pension funds and hedge funds., Their buy or sell orders may be executed on their behalf by a stock exchange trader., \n",
      "\n",
      ", Some exchanges are physical locations where transactions are carried out on a trading floor, by a method known as open outcry., This method is used in some stock exchanges and commodities exchanges, and involves traders shouting bid and offer prices., The other type of stock exchange has a network of computers where trades are made electronically., An example of such an exchange is the NASDAQ., \n",
      "\n",
      "A potential buyer bids a specific price for a stock, and a potential seller asks a specific price for the same stock., Buying or selling at the Market means you will accept any ask price or bid price for the stock., When the bid and ask prices match, a sale takes place, on a first-come, first-served basis if there are multiple bidders at a given price., \n",
      "\n",
      "The purpose of a stock exchange is to facilitate the exchange of securities between buyers and sellers, thus providing a marketplace., The exchanges provide real-time trading information on the listed securities, facilitating price discovery., \n",
      "\n",
      "The New York Stock Exchange (NYSE) is a physical exchange, with a hybrid market for placing orders electronically from any location as well as on the trading floor., Orders executed on the trading floor enter by way of exchange members and flow down to a floor broker, who submits the order electronically to the floor trading post for the Designated market maker (\"DMM\") for that stock to trade the order., The DMM's job is to maintain a two-sided market, making orders to buy and sell the security when there are no other buyers or sellers., If a bid–ask spread exists, no trade immediately takes place – in this case the DMM may use their own resources (money or stock) to close the difference., Once a trade has been made, the details are reported on the \"tape\" and sent back to the brokerage firm, which then notifies the investor who placed the order., Computers play an important role, especially for program trading., \n",
      "\n",
      "The NASDAQ is an electronic exchange, where all of the trading is done over a computer network., The process is similar to the New York Stock Exchange., One or more NASDAQ market makers will always provide a bid and ask the price at which they will always purchase or sell 'their' stock., \n",
      "\n",
      "The Paris Bourse, now part of Euronext, is an order-driven, electronic stock exchange., It was automated in the late 1980s., Prior to the 1980s, it consisted of an open outcry exchange., Stockbrokers met on the trading floor of the Palais Brongniart., In 1986, the CATS trading system was introduced, and the order matching system was fully automated., \n",
      "\n",
      "People trading stock will prefer to trade on the most popular exchange since this gives the largest number of potential counter parties (buyers for a seller, sellers for a buyer) and probably the best price., However, there have always been alternatives such as brokers trying to bring parties together to trade outside the exchange., Some third markets that were popular are Instinet, and later Island and Archipelago (the latter two have since been acquired by Nasdaq and NYSE, respectively)., One advantage is that this avoids the commissions of the exchange., However, it also has problems such as adverse selection.[7], Financial regulators have probed dark pools.[8][9], \n",
      "\n",
      "]\n"
     ]
    }
   ],
   "source": [
    "sentence_tokens = [sent for sent in doc.sents]\n",
    "print(sentence_tokens)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 57,
   "id": "wooden-hamilton",
   "metadata": {},
   "outputs": [],
   "source": [
    "sentence_scores = {}\n",
    "for sent in sentence_tokens:\n",
    "    for word in sent:\n",
    "        if word.text.lower() in word_frequencies.keys():\n",
    "            if sent not in sentence_scores.keys():\n",
    "                sentence_scores[sent] = word_frequencies[word.text.lower()]\n",
    "            else:\n",
    "                sentence_scores[sent] += word_frequencies[word.text.lower()]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 58,
   "id": "delayed-overall",
   "metadata": {},
   "outputs": [],
   "source": [
    "from heapq import nlargest"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 59,
   "id": "dutch-toddler",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "12"
      ]
     },
     "execution_count": 59,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "select_length = int(len(sentence_tokens)*0.3)\n",
    "select_length"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 60,
   "id": "cross-wichita",
   "metadata": {},
   "outputs": [],
   "source": [
    "summary = nlargest(select_length, sentence_scores, key = sentence_scores.get)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 61,
   "id": "unavailable-robert",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[Orders executed on the trading floor enter by way of exchange members and flow down to a floor broker, who submits the order electronically to the floor trading post for the Designated market maker (\"DMM\") for that stock to trade the order.,\n",
       " A stock exchange is an exchange (or bourse)[note 1] where stockbrokers and traders can buy and sell shares (equity stock), bonds, and other securities.,\n",
       " Some large companies will have their stock listed on more than one exchange in different countries, so as to attract international investors.[6]\n",
       " \n",
       " Stock exchanges may also cover other types of securities, such as fixed-interest securities (bonds) or (less frequently) derivatives, which are more likely to be traded OTC.,\n",
       " \n",
       " \n",
       " People trading stock will prefer to trade on the most popular exchange since this gives the largest number of potential counter parties (buyers for a seller, sellers for a buyer) and probably the best price.,\n",
       " \n",
       " \n",
       " The New York Stock Exchange (NYSE) is a physical exchange, with a hybrid market for placing orders electronically from any location as well as on the trading floor.,\n",
       " \n",
       " \n",
       " Trade in stock markets means the transfer (in exchange for money) of a stock or security from a seller to a buyer.,\n",
       " \n",
       " \n",
       " A potential buyer bids a specific price for a stock, and a potential seller asks a specific price for the same stock.,\n",
       " \n",
       " \n",
       " The purpose of a stock exchange is to facilitate the exchange of securities between buyers and sellers, thus providing a marketplace.,\n",
       " \n",
       " \n",
       " Participants in the stock market range from small individual stock investors to larger investors, who can be based anywhere in the world, and may include banks, insurance companies, pension funds and hedge funds.,\n",
       " Buying or selling at the Market means you will accept any ask price or bid price for the stock.,\n",
       " Their buy or sell orders may be executed on their behalf by a stock exchange trader.,\n",
       " If a bid–ask spread exists, no trade immediately takes place – in this case the DMM may use their own resources (money or stock) to close the difference.]"
      ]
     },
     "execution_count": 61,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "summary"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 62,
   "id": "therapeutic-driving",
   "metadata": {},
   "outputs": [],
   "source": [
    "final_summary = [word.text for word in summary]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 63,
   "id": "french-track",
   "metadata": {},
   "outputs": [],
   "source": [
    "summary = ' '.join(final_summary)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 64,
   "id": "accepted-lottery",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n",
      "A stock exchange is an exchange (or bourse)[note 1] where stockbrokers and traders can buy and sell shares (equity stock), bonds, and other securities. Many large companies have their stocks listed on a stock exchange. This makes the stock more liquid and thus more attractive to many investors. The exchange may also act as a guarantor of settlement. These and other stocks may also be traded \"over the counter\" (OTC), that is, through a dealer. Some large companies will have their stock listed on more than one exchange in different countries, so as to attract international investors.[6]\n",
      "\n",
      "Stock exchanges may also cover other types of securities, such as fixed-interest securities (bonds) or (less frequently) derivatives, which are more likely to be traded OTC.\n",
      "\n",
      "Trade in stock markets means the transfer (in exchange for money) of a stock or security from a seller to a buyer. This requires these two parties to agree on a price. Equities (stocks or shares) confer an ownership interest in a particular company.\n",
      "\n",
      "Participants in the stock market range from small individual stock investors to larger investors, who can be based anywhere in the world, and may include banks, insurance companies, pension funds and hedge funds. Their buy or sell orders may be executed on their behalf by a stock exchange trader.\n",
      "\n",
      "Some exchanges are physical locations where transactions are carried out on a trading floor, by a method known as open outcry. This method is used in some stock exchanges and commodities exchanges, and involves traders shouting bid and offer prices. The other type of stock exchange has a network of computers where trades are made electronically. An example of such an exchange is the NASDAQ.\n",
      "\n",
      "A potential buyer bids a specific price for a stock, and a potential seller asks a specific price for the same stock. Buying or selling at the Market means you will accept any ask price or bid price for the stock. When the bid and ask prices match, a sale takes place, on a first-come, first-served basis if there are multiple bidders at a given price.\n",
      "\n",
      "The purpose of a stock exchange is to facilitate the exchange of securities between buyers and sellers, thus providing a marketplace. The exchanges provide real-time trading information on the listed securities, facilitating price discovery.\n",
      "\n",
      "The New York Stock Exchange (NYSE) is a physical exchange, with a hybrid market for placing orders electronically from any location as well as on the trading floor. Orders executed on the trading floor enter by way of exchange members and flow down to a floor broker, who submits the order electronically to the floor trading post for the Designated market maker (\"DMM\") for that stock to trade the order. The DMM's job is to maintain a two-sided market, making orders to buy and sell the security when there are no other buyers or sellers. If a bid–ask spread exists, no trade immediately takes place – in this case the DMM may use their own resources (money or stock) to close the difference. Once a trade has been made, the details are reported on the \"tape\" and sent back to the brokerage firm, which then notifies the investor who placed the order. Computers play an important role, especially for program trading.\n",
      "\n",
      "The NASDAQ is an electronic exchange, where all of the trading is done over a computer network. The process is similar to the New York Stock Exchange. One or more NASDAQ market makers will always provide a bid and ask the price at which they will always purchase or sell 'their' stock.\n",
      "\n",
      "The Paris Bourse, now part of Euronext, is an order-driven, electronic stock exchange. It was automated in the late 1980s. Prior to the 1980s, it consisted of an open outcry exchange. Stockbrokers met on the trading floor of the Palais Brongniart. In 1986, the CATS trading system was introduced, and the order matching system was fully automated.\n",
      "\n",
      "People trading stock will prefer to trade on the most popular exchange since this gives the largest number of potential counter parties (buyers for a seller, sellers for a buyer) and probably the best price. However, there have always been alternatives such as brokers trying to bring parties together to trade outside the exchange. Some third markets that were popular are Instinet, and later Island and Archipelago (the latter two have since been acquired by Nasdaq and NYSE, respectively). One advantage is that this avoids the commissions of the exchange. However, it also has problems such as adverse selection.[7] Financial regulators have probed dark pools.[8][9]\n",
      "\n",
      "\n"
     ]
    }
   ],
   "source": [
    "print(text)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 65,
   "id": "characteristic-stake",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['Orders executed on the trading floor enter by way of exchange members and flow down to a floor broker, who submits the order electronically to the floor trading post for the Designated market maker (\"DMM\") for that stock to trade the order.', 'A stock exchange is an exchange (or bourse)[note 1] where stockbrokers and traders can buy and sell shares (equity stock), bonds, and other securities.', 'Some large companies will have their stock listed on more than one exchange in different countries, so as to attract international investors.[6]\\n\\nStock exchanges may also cover other types of securities, such as fixed-interest securities (bonds) or (less frequently) derivatives, which are more likely to be traded OTC.', '\\n\\nPeople trading stock will prefer to trade on the most popular exchange since this gives the largest number of potential counter parties (buyers for a seller, sellers for a buyer) and probably the best price.', '\\n\\nThe New York Stock Exchange (NYSE) is a physical exchange, with a hybrid market for placing orders electronically from any location as well as on the trading floor.', '\\n\\nTrade in stock markets means the transfer (in exchange for money) of a stock or security from a seller to a buyer.', '\\n\\nA potential buyer bids a specific price for a stock, and a potential seller asks a specific price for the same stock.', '\\n\\nThe purpose of a stock exchange is to facilitate the exchange of securities between buyers and sellers, thus providing a marketplace.', '\\n\\nParticipants in the stock market range from small individual stock investors to larger investors, who can be based anywhere in the world, and may include banks, insurance companies, pension funds and hedge funds.', 'Buying or selling at the Market means you will accept any ask price or bid price for the stock.', 'Their buy or sell orders may be executed on their behalf by a stock exchange trader.', 'If a bid–ask spread exists, no trade immediately takes place – in this case the DMM may use their own resources (money or stock) to close the difference.']\n"
     ]
    }
   ],
   "source": [
    "print(final_summary)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "loose-affiliate",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
