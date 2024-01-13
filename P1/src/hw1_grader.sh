#!/bin/bash
# Grading for CS 72/LING 48 HW1
echo python filename:
read varname
# varname="hello_eliza.py"
echo 
echo \>\>\> The translations are included only to help you understand the inputs
echo \>\>\> and outputs. They should NOT be included in the input and they should
echo \>\>\> NOT appear in the output.
echo 
echo 
echo ===== Q1 =====

echo ===== Name ===

echo 
echo Input: Jina langu ni Ken. \(My name is Ken\)
echo Expected output: Shikamoo, Ken. Umeshindaje? \(Hi, Ken. How are you?\)
echo Program output:
python3 $varname "Jina langu ni Ken."
echo 
echo Input: Naitwa Ken. \(I am called Ken.\)
echo Expected output: Shikamoo, Ken. Umeshindaje? \(Hi, Ken. How are you?\)
echo Program output:
python3 $varname "Naitwa Ken."
echo 
echo =========== Q2 ==========

echo ===== State of mind =====

echo 
echo Input: Nimefurahi. \(i\'m happy... :\)\)
echo Expected output: Mbona umefurahi? \(Why are you happy?\)
echo Program output:
python3 $varname "Nimefurahi."
echo 
echo Input: Sijafurahi. \(I\'m not happy.\)
echo Expected output: Mbona hujafurahi? \(Why aren\'t you happy?\)
echo Program output:
python3 $varname "Sijafurahi."
echo 
echo Input: Nimehuzunika kidogo. \(I\'m a bit sad.\)
echo Expected output: Mbona umehuzunika? \(Why are you sad?\)
echo Program output:
python3 $varname "Nimehuzunika kidogo."
echo 
echo Input: Mi nimehuzunika kidogo. \(I\'m a bit sad.\)
echo Expected output: Mbona umehuzunika? \(Why are you sad?\)
echo Program output:
python3 $varname "Mi nimehuzunika kidogo."
echo 
echo ============ Q3 ===========

echo ===== Characteristics =====

echo 
echo Input: Mimi ni mchafu. \(I\'m messy.\)
echo Expected output: Mbona wewe ni mchafu? \(Why are you messy?\)
echo Program output:
python3 $varname "Mimi ni mchafu."
echo 
echo Input: Mimi si mtu safi. \(I\'m not an orderly person.\)
echo Expected output: Mbona wewe si mtu safi? \(Why aren\'t you an orderly person?\)
echo Program output:
python3 $varname "Mimi si mtu safi."
echo 
echo Input: Mimi ni mwanafunzi wa Dartmouth. \(I\'m a Dartmouth student.\)
echo Expected output: Mbona wewe ni mwanafunzi wa Dartmouth? \(Why are you a Dartmouth student?\)
echo Program output:
python3 $varname "Mimi ni mwanafunzi wa Dartmouth."
echo 
echo Input: Ni kwamba mimi ni mchafu sana. \(It\'s just that I\'m very messy.\)
echo Expected output: Mbona wewe ni mchadu sana? \(Why are you very messy?\)
echo Program output:
python3 $varname "Ni kwamba mimi ni mchafu sana."
echo 
echo ===== Q4 ========

echo ===== Family ====

echo 
echo Input: Mamangu anapenda waridi. \(My mom likes orchids.\)
echo Expected output: Niambie mengine kumhusu mamako. \(Tell me more about your mom.\)
echo Program output:
python3 $varname "Mamangu anapenda waridi."
echo 
echo Input: Babangu hapendi kakati. \(Because my dad prefers trees.\)
echo Expected output: Niambie mengine kumhusu babako. \(Tell me more about your dad.\)
echo Program output:
python3 $varname "Babangu hapendi kakati."
echo 
echo Input: Kwa sababu mamangu yu hodari na mimea. \(Because my mom wants me to leave the house.\)
echo Expected output: Niambie mengine kumhusu mamako. \(Tell me more about your mom.\)
echo Program output:
python3 $varname "Kwa sababu mamangu yu hodari na mimea."
echo 
echo ===== Q5 =========

echo ===== Clitics ====

echo 
echo Input: Sitaki kujifunza kuandika msimbo. \(i don\'t want to learn how to program\)
echo Expected output: Mbuna hutaki kujifunza kuandika msimbo? \(Why don\'t you want to learn how to program?\)
echo Program output:
python3 $varname "Sitaki kujifunza kuandika msimbo."
echo 
echo Input: Rafiki yangu amesema naweza kula vidakuzi kumi. \(i can eat like ten cookies.\)
echo Expected output: Mbona unaweza kula vidakuzi kumi? \(Why can you eat ten cookies?\)
echo Program output:
python3 $varname "Rafiki yangu amesema naweza kula vidakuzi kumi."
echo 
echo Input: Sitaki kuenda safari! \(I don\'t want to go on a trip!\)
echo Expected output: Mbona hutaki kuenda safari? \(Why don\'t you want to go on a trip?\)
echo Program output:
python3 $varname "Sitaki kuenda safari!"
echo 
echo Input: Naweza kutembea kwenye theluji. \(I can walk in the snow.\)
echo Expected output: Mbona unaweza kutembea kwenye theluji? \(Why can you walk in the snow?\)
echo Program output:
python3 $varname "Naweza kutembea kwenye theluji."
echo 
echo Input: Amesema nahitaji kusafisha chumba changu. \(She says I need to tidy up the room.\)
echo Expected output: Mbona unahitaji kusafisha chumba chako? \(Why do you need to tidy up the room?\)
echo Program output:
python3 $varname "Amesema nahitaji kusafisha chumba changu."
echo 
echo ===== Q6 ====================

echo ===== Thoughts and hopes ====

echo 
echo Input: Nadhani rafiki zangu walifanya hivo pia. \(I think my friends did that too.\)
echo Expected output: Mbona unadhani hivyo? \(Why do you think that?\)
echo Program output:
python3 $varname "Nadhani rafiki zangu walifanya hivo pia."
echo 
echo Input: Natumai kuhitimu mwaka ujao. \(I hope to graduate next year.\)
echo Expected output: Mbona unatumai hivyo? \(Why do you hope that?\)
echo Program output:
python3 $varname "Natumai kuhitimu mwaka ujao."
echo 
echo Input: Nadhani yote yalianza nilipoenda pwani mara ya kwanza. \(I think it all began when I went to the beach for the first time.\)
echo Expected output: Mbona unadhani hivyo? \(Why do you think that?\)
echo Program output:
python3 $varname "Nadhani yote yalianza nilipoenda pwani mara ya kwanza."
echo 
echo ===== Q7 ====================

echo ===== Asking for examples ===

echo 
echo Input: Yeye husema hivo tu. \(He always says the same thing.\)
echo Expected output: Unaweza nipa mfano? \(Can you give me a specific example?\)
echo Program output:
python3 $varname "Yeye husema hivo tu."
echo 
echo Input: Kakangu hula vidakuzi. \(My brother always eats the cookies.\)
echo Expected output: Unaweza nipa mfano? \(Can you give me a specific example?\)
echo Program output:
python3 $varname "Kakangu hula vidakuzi."
echo 
echo ===== Q8 ====================

echo ===== Handling insults ======

echo 
echo Input: Hapana, mshenzi! \(No, stupid!\)
echo Expected output: Ha! Matusi hapana! Tulia na uniambie mengine \(Hey, no insults! Calm down and tell me more.\)
echo Program output:
python3 $varname "Hapana, mshenzi!"
echo 
echo Input: Wewe ni mjinga. \(You\'re an idiot\)
echo Expected output: Ha! Matusi hapana! Tulia na uniambie mengine \(Hey, no insults! Calm down and tell me more.\)
echo Program output:
python3 $varname "Wewe ni mjinga."
echo 
echo ===== Q9 ====================

echo ===== Generic reply =========

echo 
echo Input: Kujichocha! \(Because I wanna!\)
echo Expected output: Niambie mengine... \(Tell me more.\)
echo Program output:
python3 $varname "Kujichocha!"
echo 
