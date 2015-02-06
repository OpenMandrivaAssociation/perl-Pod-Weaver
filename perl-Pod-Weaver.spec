%define upstream_name    Pod-Weaver
%define upstream_version 4.006

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	3

Summary:	A bundle for the most commonly-needed prep work for a pod document
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Pod/Pod-Weaver-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Config::INI)
BuildRequires:	perl(Config::MVP::Reader::INI)
BuildRequires:	perl(Config::MVP)
BuildRequires:	perl(DateTime)
BuildRequires:	perl(List::MoreUtils)
BuildRequires:	perl(Log::Dispatchouli)
BuildRequires:	perl(Moose)
BuildRequires:	perl(Moose::Autobox)
BuildRequires:	perl(PPI)
BuildRequires:	perl(Pod::Elemental)
BuildRequires:	perl(Pod::Eventual::Simple)
BuildRequires:	perl(Software::License)
BuildRequires:	perl(String::Flogger)
BuildRequires:	perl(String::RewritePrefix)
BuildRequires:	perl(String::Formatter)
BuildRequires:	perl(Test::Differences)
BuildRequires:	perl(namespace::autoclean)

BuildArch:	noarch

%description
Pod::Weaver is a system for building Pod documents from templates. It
doesn't perform simple text substitution, but instead builds a
Pod::Elemental::Document. Its plugins sketch out a series of sections that
will be produced based on an existing Pod document or other provided
information.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc Changes LICENSE README
%{_mandir}/man3/*
%{perl_vendorlib}/*

%changelog
* Sat Apr 23 2011 Funda Wang <fwang@mandriva.org> 3.101.632-2mdv2011.0
+ Revision: 657326
- tweak br
- rebuild for updated spec-helper

* Thu Nov 11 2010 Guillaume Rousse <guillomovitch@mandriva.org> 3.101.632-1mdv2011.0
+ Revision: 596068
- update to new version 3.101632

* Wed Jul 14 2010 Jérôme Quelin <jquelin@mandriva.org> 3.101.630-1mdv2011.0
+ Revision: 553154
- update to 3.101630

* Sun Mar 14 2010 Jérôme Quelin <jquelin@mandriva.org> 3.100.710-1mdv2010.1
+ Revision: 518828
- adding missing buildrequires:
- update to 3.100710

* Wed Mar 10 2010 Jérôme Quelin <jquelin@mandriva.org> 3.100.680-1mdv2010.1
+ Revision: 517306
- update to 3.100680

* Sun Mar 07 2010 Jérôme Quelin <jquelin@mandriva.org> 3.100.650-1mdv2010.1
+ Revision: 515370
- update to 3.100650

* Mon Feb 01 2010 Jérôme Quelin <jquelin@mandriva.org> 3.100.310-1mdv2010.1
+ Revision: 498983
- update to 3.100310

* Mon Dec 21 2009 Jérôme Quelin <jquelin@mandriva.org> 3.93.530-1mdv2010.1
+ Revision: 480736
- update to 3.093530

* Tue Nov 10 2009 Jérôme Quelin <jquelin@mandriva.org> 3.93.130-1mdv2010.1
+ Revision: 463915
- update to 3.093130
- using buildrequires that upstream chose to elect as prereq when bug was reported

* Mon Nov 09 2009 Jérôme Quelin <jquelin@mandriva.org> 3.93.120-1mdv2010.1
+ Revision: 463522
- fix buildrequires
- adding missing buildrequires:
- update to 3.093120
- import perl-Pod-Weaver


* Sun Nov 08 2009 cpan2dist 3.093001-1mdv
- initial mdv release, generated with cpan2dist



