Summary: An Alpha tool for removing debugging information from kernel images.
Name: quickstrip
Version: 1.1
Release: 6
ExclusiveArch: alpha
Copyright: distributable
Group: Development/Tools
Source: quickstrip-1.1.tar.gz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The quickstrip utility strips symbolic debugging information from
Linux/Alpha ECOFF binaries.  The standard strip utility has occasional
problems with ECOFF binaries (especially, for example, with kernel
images), so quickstrip is used instead.

%prep
%setup -q

%build
make CFLAGS="$RPM_OPT_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/{bin,man/man1}

make install
install -m 755 -s quickstrip $RPM_BUILD_ROOT/usr/bin/quickstrip
install -m 644 quickstrip.1 $RPM_BUILD_ROOT/usr/man/man1/quickstrip.1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
/usr/bin/quickstrip
/usr/man/man1/quickstrip.1
