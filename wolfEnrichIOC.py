#############################################################################################################################################
"""
User case:
You are a security enginee/Analyst you are 
1. Reviewing all the approved domains, urls, IPAddress in the native or firewall Allow list( such as MDE allow list, Palo alto)
2. Investigating incident and you got 100s of IOCs, it may be rare but possible, in this case what if you can get some costom details of all the iocs to analyze.
3. So this code will just pick any random data, parse and give you clean iocs and the malicious score Phew. """
#############################################################################################################################################
"""
=>>>> WHAT'S NEXT:
In this next code, I’ll use Python to analyze lateral movement techniques. I’ll focus on detecting suspicious activity from processes 
like wmiprvse.exe, powershell.exe, wsmprovhost.exe, and psexec.exe, as well as network protocols commonly abused for lateral movement 
such as SMB, RDP, and LDAP. Aligning these indicators with MITRE ATT&CK frameworks will help identify attack patterns systematically.
Key processes to monitor include explorer.exe, svchost.exe, cmd.exe, WmiApSrv.exe, services.exe, mstsc.exe, rdpclip.exe, schtasks.exe, 
taskeng.exe, lsass.exe, procdump.exe, and mimikatz.exe. Combined with protocol analysis for SMB, WinRM, and LDAP, this approach aids in 
early detection of lateral movement and persistence across endpoints.
"""
#########################################################################################################################################

# if i get so many iocs, and unstructured, i will dump it to note, which would be txt. we can do it in csv, but I am choosing what i usually would do 
IOCs = "bulk_ioc.txt" # change the name of the file

# in progress
