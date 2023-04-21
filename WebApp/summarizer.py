import spacy
from spacy.lang.en.stop_words import STOP_WORDS
from heapq import nlargest
from string import punctuation


def summarizer(article):
    stopwords=list(STOP_WORDS)
    # article=""" Syria (Arabic: سُورِيَا or سُورِيَة, romanized: Sūriyā), officially the Syrian Arab Republic (Arabic: الجمهورية العربية السورية, romanized
    # : al-Jumhūrīyah al-ʻArabīyah as-Sūrīyah), is a Western Asian country located in the Eastern Mediterranean and the Levant. It is a unitary republic 
    # that consists of 14 governorates (subdivisions), and is bordered by the Mediterranean Sea to the west, Turkey to the north, Iraq to the east and southeast,
    # Jordan to the south, and Israel and Lebanon to the southwest. Cyprus lies to the west across the Mediterranean Sea. A country of fertile plains, 
    # high mountains, and deserts, Syria is home to diverse ethnic and religious groups, including the majority Syrian Arabs, Kurds, Turkmens, Assyrians, 
    # Circassians,[11] Armenians, Albanians, Greeks, and Chechens. Religious groups include Muslims, Christians, Alawites, Druze, and Yazidis. 
    # The capital and largest city of Syria is Damascus. Arabs are the largest ethnic group, and Sunni Muslims are the largest religious group. 
    # Syria is the only country that is governed by Ba'athists, who advocate Arab socialism and Arab nationalism. Syria is a member of the Non-Aligned Movement.
    # The name "Syria" historically referred to a wider region, broadly synonymous with the Levant,[12] and known in Arabic as al-Sham. The modern 
    # state encompasses the sites of several ancient kingdoms and empires, including the Eblan civilization of the 3rd millennium BC. Aleppo and 
    # the capital city Damascus are among the oldest continuously inhabited cities in the world.[13] In the Islamic era, Damascus was the seat 
    # of the Umayyad Caliphate and a provincial capital of the Mamluk Sultanate in Egypt. The modern Syrian state was established in the mid-20th 
    # century after centuries of Ottoman rule. After a period as a French mandate (1923–1946), the newly-created state represented the largest 
    # Arab state to emerge from the formerly Ottoman-ruled Syrian provinces. It gained de jure independence as a democratic parliamentary republic
    # on 24 October 1945 when the Republic of Syria became a founding member of the United Nations, an act which legally ended the former French 
    # mandate (although French troops did not leave the country until April 1946).The post-independence period was tumultuous, with multiple 
    # military coups and coup attempts shaking the country between 1949 and 1971. In 1958, Syria entered a brief union with Egypt called the 
    # United Arab Republic, which was terminated by the 1961 Syrian coup d'état. The republic was renamed as the Arab Republic of Syria in late
    # 1961 after the December 1 constitutional referendum of that year. A significant event was the 1963 coup d'état carried out by the military
    # committee of the Arab Socialist Ba'ath Party which established a one-party state. It ran Syria under emergency law from 1963 to 2011, 
    # effectively suspending constitutional protections for citizens. Internal power-struggles within neo-Ba'athist factions caused further 
    # coups in 1966 and 1970, which eventually resulted in the seizure of power by General Hafez al-Assad. Assad assigned Alawite loyalists 
    # to key posts in the armed forces, bureaucracy, Mukhabarat and the ruling elite; effectively establishing an "Alawi minority rule" to 
    # consolidate power within his family.[14]. After the death of Hafez al-Assad in 2000, his son Bashar al-Assad inherited the presidency
    # and political system centered around a cult of personality to the al-Assad family.[15] The Ba'ath regime has been condemned for numerous 
    # rights abuses, including frequent executions of citizens and political prisoners, massive censorship[16][17] and for financing 
    # a multi-billion dollar illicit drug trade.[18][19] Following its violent suppression of the Arab Spring protests of the 2011 
    # Syrian Revolution, the Syrian government was suspended from the Arab League in November 2011[20] and quit the Union for the 
    # Mediterranean the following month.[21] Since July 2011, Syria has been embroiled in a multi-sided civil war, with the involvement 
    # of different countries. The Organisation of Islamic Cooperation suspended Syria in August 2012 citing "deep concern at the massacres and
    # inhuman acts" perpetrated by forces loyal to Bashar al-Assad.[a] As of 2020, three political entities – the Syrian Interim Government, 
    # Syrian Salvation Government, and Autonomous Administration of North and East Syria – have emerged in Syrian territory to challenge Assad's rule.
    # Syria was ranked last on the Global Peace Index from 2016 to 2018,[23] making it the most violent country in the world due to the war.
    # Syria is the most corrupt country in the MENA region and was ranked the second lowest globally on the 2022 Corruption Perceptions Index.[b] 
    # The Syrian civil war has killed more than 570,000 people,[24] with pro-Assad forces causing more than 90% of the total civilian casualties.[c] 
    # The war led to the Syrian refugee crisis, with an estimated 7.6 million internally displaced people (July 2015 UNHCR figure) and over 5 million
    # refugees (July 2017 registered by UNHCR),[33] making population assessment difficult in recent years. The war has also worsened economic
    # conditions, with more than 90% of the population living in poverty and 80% facing food insecurity.[d]"""

    nlp=spacy.load('en_core_web_sm')
    doc=nlp(article)
    tokens=[token.text for token in doc]
    # print(tokens)
    word_frequencies={}
    for word in doc:
        if word.text.lower() not in stopwords:
            if word.text.lower() not in punctuation:
                if word.text not in word_frequencies.keys():
                    word_frequencies[word.text]=1
                else:
                    word_frequencies[word.text]+=1
    # print(word_frequencies)


    max_frequency=max(word_frequencies.values())

    for word in word_frequencies.keys():
        word_frequencies[word]=word_frequencies[word]/max_frequency

    sentence_tokens=[sent for sent in doc.sents]


    sentence_scores={}
    for sent in sentence_tokens:
        for word in sent:
            if word.text.lower() in word_frequencies.keys():
                if sent not in sentence_scores.keys():
                    sentence_scores[sent]=word_frequencies[word.text.lower()]
                else:
                    sentence_scores[sent]+=word_frequencies[word.text.lower()]

    select_length=int(len(sentence_tokens)*0.3)

    summary=nlargest(select_length,sentence_scores,key=sentence_scores.get)
    final_summary=[word.text for word in summary]
    summary=' '.join(final_summary)
    doc_length=len(article.split(' '))
    summary_length=len(summary.split(' '))
    
    return  doc, doc_length, summary, summary_length



      

