
# Conditional build:
%bcond_without	tests	# do not perform "make test"

%include	/usr/lib/rpm/macros.perl
%define	pdir	Module
%define	pnam	Signature
Summary:	Module signature file manipulation
Name:		perl-Module-Signature
Version:	0.36
Release:	1
License:	Same as Perl Itself
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	92ac8341cc6973edb700fae476b0ffc1
BuildRequires:	perl-devel >= 5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-Digest-SHA1
%endif
# gnupg or Crypt::OpenPGP
BuildRequires:	gnupg
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Module::Signature adds cryptographic authentications to CPAN
distributions, via the special SIGNATURE file.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
echo 3 | %{__perl} Makefile.PL \
	INSTALLDIRS=vendor \
	--skipdeps

%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/Module/*
%{_mandir}/man3/*
%{_mandir}/man1/*
%attr(755,root,root) %{_bindir}/cpansign
