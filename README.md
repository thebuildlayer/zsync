Overview
===

zsync is a file transfer program. It allows you to download a file from a remote server, where you have a copy of an older version of the file on your computer already. zsync downloads only the new parts of the file. It uses the same algorithm as rsync. 

However, where rsync is designed for synchronising data from one computer to another within an organisation, zsync is designed for file distribution, with one file on a server to be distributed to thousands of downloaders. zsync requires no special server software — just a web server to host the files — and imposes no extra load on the server, making it ideal for large scale file distribution.

zsync is open source, distributed under version 2 of the Artistic License. Feedback, bugs reports and patches are welcome.

Notes from the build team
===
- This is the first build of zsync. No license was included in the archive, however we have included one here
- To install this package you need to have the [TBL Repo](https://tbl.mirrors.theom.nz/BuildService/7/x86_64/tbl-release-7-0.noarch.rpm) installed
