Name:           zsync
Version:        0.6.2
Release:        1%{?dist}
Summary:        zsync is a file transfer program similar to rsync

License:        GPLv2+
URL:            http://zsync.moria.org.uk/index
Source0:        http://zsync.moria.org.uk/download/zsync-0.6.2.tar.bz2

%description
zsync is a file transfer program. It allows you to download a file from a remote server,
where you have a copy of an older version of the file on your computer already.

%prep
%setup -q


%build
%configure
./configure --prefix=/usr
make %{?_smp_mflags}

%check
make check

%install
rm -rf $RPM_BUILD_ROOT
%make_install


%files
%doc COPYING README
%{_bindir}/*
%{_mandir}/man1/*
%{_docdir}/zsync/*

%changelog
* Thu Apr 11 2019 Theo Morra <theo@morra.nz> - 0.6.2
- initial zsync build
