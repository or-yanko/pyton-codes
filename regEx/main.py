#or yanko
import re
text = """call 0501234567 in 12.12.1212. Right now, it’s challenging to look forward to what 2021 will bring with any degree of clarity – even from a 
business context. Covid-19 has already altered nearly every aspect of how organisations operate; from the distribution 
of workforces, to the movement of almost all customer interactions online, the business world has completely turned on 
its head. 
One thing we do know is that these changes have dramatically accelerated digital initiatives across industries.
 Technologies to help productivity and business continuity have flourished. Whether it is bringing on new collaboration 
 tools or moving critical infrastructure and applications to the cloud, IT has become more distributed – and as a 
 result, the range of opportunities for attackers has significantly increased. 
So as we look ahead to 2021, how exactly will the convergence of these unimaginable forces and events impact 
cybersecurity for the next 12 months? 

Attackers’ tactics will evolve as personal islands of security form
companies’ adoption of longer-term remote work strategies means distributed IT environments will only continue to 
expand. With many employees working from home, they are regularly accessing corporate systems and resources through
 insecure home networks and personal devices. This makes each user their own island, rendering legacy security controls
 ineffective. Individual actions are threatening corporate security to a greater degree than ever before. 
It’s because of these islands of security that we’ll see the attack cycle move away from broad ‘spray and pray’ 
social-engineering attacks to more hyper-personalised ones. These attacks will target those users with privileged 
access to sensitive systems, data and infrastructure. 
Where attackers generally rely on lateral movement, seeking any foothold and working to elevate access and move across 
the network to get to their desired destination, these islands now limit the attacker to whatever high levels of access
 their specific target has been granted. As a result, we’ll see a move toward vertical movement, with attackers
targeting individuals, like business users, based on what they have access to – from administrative consoles and 
financial records, to competitive data. 
While this new ‘personalised attack chain’ approach will be more time consuming and costly for attackers as they look
 to identify and profile the exact person they are looking for, it will also lead to shorter attack-cycles. This may
 make it more difficult for organisations to identify and stop attacks before they impact the business.
"""


#1. כל המילים שמתחילות באות b
startWithB = re.split(" ", text)
print("1:\n")
for word in startWithB:
    if word[0] == 'b':
        print(word)

#2. כמה משפטים יש בטקסט (משפטים מסתיימים ב- '.' או ',' או '?' או '!'.
countSen = 0
countSen += text.count(',')
countSen += text.count('.')
countSen += text.count('?')
countSen += text.count('!')
print("\n\n2:")
print(countSen)

#3. חלצו את כל המספרים מהטקסט (ספרות ברצף (לדוגמה: 1953, 28, 01, 5000, 7)).
numbersSum = re.findall('([1-9]+)', text)
print("\n\n3:")
print(numbersSum)

#4. חלצו את כל המילים שיש בהן את האותיות ("a"', "e", "i", "o").
beg = re.findall(' ' + '([' + 'aeio' + '][a-zA-Z]+)', text)
mid = re.findall('(' + '[a-zA-Z]+[' + 'aeio' + '][a-zA-Z]+)', text)
end = re.findall('(' + '[a-zA-Z]+[' + 'aeio' + ']) ', text)
print("\n\n4:")
print(beg+mid+end)

#5. מצאו מספרי טלפון.
print("\n\n5:")
print(re.findall('[0-9]{10}', text) + re.findall('[0-9]{3}[ -][0-9]{3}[ -][0-9]{4}', text))

#6. מצאו תאריכים.
print("\n\n6:")
print(re.findall('[0-3][1-9][ \.-][0-1][1-9][ \.-][0-9]{4}', text))