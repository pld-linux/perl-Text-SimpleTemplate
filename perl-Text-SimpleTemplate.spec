%include	/usr/lib/rpm/macros.perl
%define	pdir	Text
%define	pnam	SimpleTemplate
Summary:	Text::SimpleTemplate - Yet another module for template processing
Summary(pl):	Text::SimpleTemplate - jeszcze jeden modu³ do przetwarzania szablonów
Name:		perl-Text-SimpleTemplate
Version:	0.36
Release:	3
License:	GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 4.0.2-104
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is yet another library for template-based text generation.

%description -l pl
To jest jeszcze jedna biblioteka do bazuj±cego na szablonach
generowania tekstu.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.TXT
%{perl_sitelib}/Text/SimpleTemplate.pm
%{_mandir}/man3/*
