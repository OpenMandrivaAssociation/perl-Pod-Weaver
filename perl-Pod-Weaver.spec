%define upstream_name    Pod-Weaver
%define upstream_version 3.093530

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:    A bundle for the most commonly-needed prep work for a pod document
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Pod/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(Config::MVP::Reader::INI)
BuildRequires: perl(Config::MVP)
BuildRequires: perl(List::MoreUtils)
BuildRequires: perl(Moose)
BuildRequires: perl(Moose::Autobox)
BuildRequires: perl(PPI)
BuildRequires: perl(Pod::Elemental)
BuildRequires: perl(Pod::Eventual::Simple)
BuildRequires: perl(Software::License)
BuildRequires: perl(String::Flogger)
BuildRequires: perl(String::RewritePrefix)
BuildRequires: perl(Test::Differences)
BuildRequires: perl(namespace::autoclean)

BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

%description
Pod::Weaver is a system for building Pod documents from templates. It
doesn't perform simple text substitution, but instead builds a
Pod::Elemental::Document. Its plugins sketch out a series of sections that
will be produced based on an existing Pod document or other provided
information.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor

%{make}

%check
%{make} test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc Changes LICENSE README
%{_mandir}/man3/*
%perl_vendorlib/*
