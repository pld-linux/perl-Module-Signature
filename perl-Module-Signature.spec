#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Module
%define	pnam	Signature
Summary:	Module::Signature - Module signature file manipulation
Summary(pl):	Module::Signature - Obróbka pliku sygnatury modu³u
Name:		perl-Module-Signature
Version:	0.38
Release:	1
# same as perl
License:	GPL or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	679660f7a4ca7fa2a95a8167824b8024
# gnupg or Crypt::OpenPGP
BuildRequires:	gnupg
%if %{with tests}
BuildRequires:	perl-Digest-SHA1
%endif
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
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
%{__perl} Makefile.PL \
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
%{perl_vendorlib}/Module/Signature.pm
%{_mandir}/man3/*
%{_mandir}/man1/*
