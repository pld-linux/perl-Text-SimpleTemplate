#
# Conditional build:
%bcond_without	tests	# do not perform "make test"

%define		pdir	Text
%define		pnam	SimpleTemplate
%include	/usr/lib/rpm/macros.perl
Summary:	Text::SimpleTemplate - yet another module for template processing
Summary(pl.UTF-8):	Text::SimpleTemplate - jeszcze jeden moduł do przetwarzania szablonów
Name:		perl-Text-SimpleTemplate
Version:	0.36
Release:	5
License:	GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	a2f05921270b96d8e8d21b263f22e3cc
URL:		http://search.cpan.org/dist/Text-SimpleTemplate/
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is yet another library for template-based text generation.

%description -l pl.UTF-8
To jest jeszcze jedna biblioteka do bazującego na szablonach
generowania tekstu.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
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
%doc README.TXT
%{perl_vendorlib}/Text/SimpleTemplate.pm
%{_mandir}/man3/*
