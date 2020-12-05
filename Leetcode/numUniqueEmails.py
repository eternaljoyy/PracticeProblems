def numUniqueEmails(emails):
	emailSet = set() 
	
	for item in emails:
		#split the email into a local part & domain part
		localEmail, domainEmail = item.split('@')
		for i in localEmail:
			if(i == '+'):
				localEmail = localEmail[:localEmail.index(i)]
				break
			else:
				if(i == '.'):
					localEmail = localEmail.replace('.', "")
		#add to set
		emailSet.add(localEmail+'@'+domainEmail)
	return len(emailSet)


'''print(numUniqueEmails(["test.email+alex@leetcode.com",
	"test.e.mail+bob.cathy@leetcode.com",
	"testemail+david@lee.tcode.com"])) '''


print(numUniqueEmails(["fg.r.u.uzj+o.pw@kziczvh.com",
	"r.cyo.g+d.h+b.ja@tgsg.z.com","fg.r.u.uzj+o.f.d@kziczvh.com",
	"r.cyo.g+ng.r.iq@tgsg.z.com","fg.r.u.uzj+lp.k@kziczvh.com",
	"r.cyo.g+n.h.e+n.g@tgsg.z.com","fg.r.u.uzj+k+p.j@kziczvh.com",
	"fg.r.u.uzj+bw.y+@kziczvh.com","r.cyo.g+x+d.c+f.t@tgsg.z.com",
	"r.cyo.g+x+t.y.l.i@tgsg.z.com","r.cyo.g+brxxi@tgsg.z.com",
	"r.cyo.g+z+dr.k.u@tgsg.z.com","r.cyo.g+d+l.c.n+g@tgsg.z.com",
	"fg.r.u.uzj+vq.o@kziczvh.com","fg.r.u.uzj+uzq@kziczvh.com",
	"fg.r.u.uzj+mvz@kziczvh.com","fg.r.u.uzj+taj@kziczvh.com",
	"fg.r.u.uzj+fek@kziczvh.com"]))


