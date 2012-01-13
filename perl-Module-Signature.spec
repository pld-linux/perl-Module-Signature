#
# Conditional build:
%bcond_with	tests	# perform "make test" (uses network)
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Module
%define		pnam	Signature
Summary:	Module::Signature - module signature file manipulation
Summary(pl.UTF-8):	Module::Signature - obróbka pliku sygnatury modułu
Name:		perl-Module-Signature
Version:	0.68
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Module/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	c63c0b5c4e7162fc0c44512e1f832e5e
URL:		http://search.cpan.org/dist/Module-Signature/
# gnupg or Crypt::OpenPGP
BuildRequires:	gnupg
%if %{with tests}
BuildRequires:	gnupg-plugin-keys_hkp
BuildRequires:	perl-Digest-SHA1
%endif
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Module::Signature adds cryptographic authentications to CPAN
distributions, via the special SIGNATURE file.

%description -l pl.UTF-8
Module::Signature dodaje uwierzytelnianie kryptograficzne do
dystrybucji CPAN poprzez specjalny plik SIGNATURE.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
echo n | %{__perl} Makefile.PL \
	INSTALLDIRS=vendor \
	--skipdeps

%{__make}

%if %{with tests}
# ugly?
mkdir -p ~/.gnupg
%{__make} test
%endif 

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
