#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-IO-stringy
Version  : 2.111
Release  : 27
URL      : http://search.cpan.org/CPAN/authors/id/D/DS/DSKOLL/IO-stringy-2.111.tar.gz
Source0  : http://search.cpan.org/CPAN/authors/id/D/DS/DSKOLL/IO-stringy-2.111.tar.gz
Summary  : ~
Group    : Development/Tools
License  : Artistic-1.0-Perl
Requires: perl-IO-stringy-license = %{version}-%{release}
Requires: perl-IO-stringy-perl = %{version}-%{release}
BuildRequires : buildreq-cpan

%description
NAME
IO-stringy - I/O on in-core objects like strings and arrays
SYNOPSIS
IO::
::AtomicFile   adpO  Write a file which is updated atomically     ERYQ
::Lines        bdpO  I/O handle to read/write to array of lines   ERYQ
::Scalar       RdpO  I/O handle to read/write to a string         ERYQ
::ScalarArray  RdpO  I/O handle to read/write to array of scalars ERYQ
::Wrap         RdpO  Wrap old-style FHs in standard OO interface  ERYQ
::WrapTie      adpO  Tie your handles & retain full OO interface  ERYQ

%package dev
Summary: dev components for the perl-IO-stringy package.
Group: Development
Provides: perl-IO-stringy-devel = %{version}-%{release}
Requires: perl-IO-stringy = %{version}-%{release}

%description dev
dev components for the perl-IO-stringy package.


%package license
Summary: license components for the perl-IO-stringy package.
Group: Default

%description license
license components for the perl-IO-stringy package.


%package perl
Summary: perl components for the perl-IO-stringy package.
Group: Default
Requires: perl-IO-stringy = %{version}-%{release}

%description perl
perl components for the perl-IO-stringy package.


%prep
%setup -q -n IO-stringy-2.111
cd %{_builddir}/IO-stringy-2.111

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-IO-stringy
cp %{_builddir}/IO-stringy-2.111/COPYING %{buildroot}/usr/share/package-licenses/perl-IO-stringy/77f4c7d573f083f13b0ef3ce19e7836995c91ebf
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/IO::AtomicFile.3
/usr/share/man/man3/IO::InnerFile.3
/usr/share/man/man3/IO::Lines.3
/usr/share/man/man3/IO::Scalar.3
/usr/share/man/man3/IO::ScalarArray.3
/usr/share/man/man3/IO::Stringy.3
/usr/share/man/man3/IO::Wrap.3
/usr/share/man/man3/IO::WrapTie.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-IO-stringy/77f4c7d573f083f13b0ef3ce19e7836995c91ebf

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/*
