
# Conditional build:
%bcond_without	tests	# do not perform "make test"

%include	/usr/lib/rpm/macros.perl
%define	pdir	Module
%define	pnam	Signature
Summary:	Module signature file manipulation
Summary(pl):	Obróbka pliku sygnatury modu³u
Name:		perl-Module-Signature
Version:	0.37
Release:	1
# same as perl
License:	GPL or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	6f4c80acffc74b96750dcf923e8adf57
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

%description -l pl
Module::Signature dodaje uwierzytelnianie kryptograficzne do
dystrybucji CPAN poprzez specjalny plik SIGNATURE.

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
%attr(755,root,root) %{_bindir}/cpansign
%{perl_vendorlib}/Module/*
%{_mandir}/man3/*
%{_mandir}/man1/*
