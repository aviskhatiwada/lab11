#!/venv/bin/python3

import glob
menu='''
1. Student grade
2. Assignment statistics
3. Assignment graph 
'''

with open('./data/students.txt') as s: 
	id_n=[(_[0:3], _[3:].strip()) for _ in s.readlines()]

with open('./data/assignments.txt') as a: 
	a=[l.strip() for l in a.readlines()]
	a_id_pt=[a[i:i+3] for i in range(0, len(a),3)]

sid_aid_per=[]
for f in glob.glob('./data/submissions/*'):
	with open(f) as s: sid_aid_per.append(s.read().split('|'))


def main():
	#id_n, a_id_pt, sid_aid_per
	#print(id_n)
	opt=int(input('Enter your selection: '))
	if opt==1:
		sn=input("What is the student's name: ")
		if sn not in [n for (_,n) in id_n]:
			print("Student not found")
		else:
			#print(sid_aid_per);exit()
			P=0
			id_=[id for id,n in id_n if n==sn][0]
			sa_per=[(sid,a,p) for (sid,a,p) in sid_aid_per if sid==id_]
			for (_,aid,pt) in a_id_pt:
				for (s,a,per) in sa_per:
					if a==aid:
						P+=int(pt)*(float(per)/1e3)

			print(str(round(P))+'%')



			#for _ in [per*int(([pt for (_,aid,pt) in a_id_pt if aid==aid_][0])) for k(sid,aid_,per) in sid_aid_per if sid==id_]:


if __name__=="__main__":
	main()

