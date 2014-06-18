
Summary:        OSCAR Configurator.
Name:           configurator
Version:        1.0.8
Release:        1
Vendor:         Open Cluster Group <http://OSCAR.OpenClusterGroup.org/>
Distribution:   OSCAR
Packager:       Geoffroy Vallee <valleegr@ornl.gov>
License:        GPL
Group:          Development/Libraries
Source:         %{name}.tar.gz
BuildRoot:      %{_localstatedir}/tmp/%{name}-root
BuildArch:      noarch
Requires:       oda >= 1.4.5

%description
Set of scripts and Perl modules for the OSCAR Configurator.

%prep
%setup -n %{name}

%build

%install 
make install DESTDIR=$RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%{perl_vendorlib}/OSCAR/*

%changelog
* Wed Jun 18 2014 Olivier Lahaye <olivier.lahaye@cea.fr> 1.0.8-1
- New upstream version (see ChangeLog for more details).
* Tue Feb 18 2014 Olivier Lahaye <olivier.lahaye@cea.fr> 1.0.7-1
- New upstream version (see ChangeLog for more details).
* Sun Dec 15 2013 Olivier Lahaye <olivier.lahaye@cea.fr> 1.0.6-2
- Fixed packaging: no more need to use the SEDLIBDIR.
- Avoid owning %{perl_vendorlib}/OSCAR (owned by oscar-base-lib)
* Mon Dec 02 2013 Olivier Lahaye <olivier.lahaye@cea.fr> 1.0.6-1
- New upstream version (see ChangeLog for more details).
* Tue Nov 24 2009 Geoffroy Vallee <valleegr@ornl.gov> 1.0.5-1
- New upstream version (see ChangeLog for more details).
* Tue Nov 24 2009 Geoffroy Vallee <valleegr@ornl.gov> 1.0.4-1
- New upstream version (see ChangeLog for more details).
* Fri Sep 25 2009 Geoffroy Vallee <valleegr@ornl.gov> 1.0.3-1
- New upstream version (see ChangeLog for more details).
* Thu May 07 2009 Geoffroy Vallee <valleegr@ornl.gov> 1.0.2-1
- New upstream version (see ChangeLog for more details).
* Tue Feb 10 2009 Geoffroy Vallee <valleegr@ornl.gov> 1.0.1-1
- New upstream version (see ChangeLog for more details).
* Thu Jan 08 2009 Geoffroy Vallee <valleegr@ornl.gov> 1.0-1
- New upstream version (see ChangeLog for more details).
