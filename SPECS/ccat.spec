%define debug_package %{nil}

%global gh_user     jingweno
%global gh_commit   aa20cb67b32b262d3ee14ca1239da93b05c9bde9
%global gh_short    %(c=%{gh_commit}; echo ${c:0:7})

# see https://fedoraproject.org/wiki/PackagingDrafts/Go#Build_ID
%global _dwz_low_mem_die_limit 0
%if ! 0%{?gobuild:1}
%define gobuild(o:) go build -ldflags "${LDFLAGS:-} -B 0x$(head -c20 /dev/urandom|od -An -tx1|tr -d ' \\n') " -i -v -x %{?**};
%endif

Name:           ccat
Version:        1.1.0
Release:        1%{?dist}
Summary:        ccat is the colorizing cat. It works similar to cat but displays content with syntax highlighting.
Group:          Applications/System
License:        MIT
URL:            https://github.com/%{gh_user}/%{name}
Source0:        https://github.com/%{gh_user}/%{name}/archive/v%{version}.tar.gz
BuildRequires:  golang

%description
Supported languages:
- JavaScript
- Java
- Ruby
- Python
- Go
- C
- JSON

%prep
wget https://github.com/%{gh_user}/%{name}/archive/v%{version}.tar.gz
tar xzf v%{version}.tar.gz

mkdir -p %{_builddir}/src/github.com/%{gh_user}/
cd %{_builddir}/src/github.com/%{gh_user}/
ln -snf %{_builddir}/%{name}-%{version} %{name}
cd %{name}

%build
export GOPATH="%{_builddir}"
export PATH=$PATH:"%{_builddir}"/bin
cd %{_builddir}/src/github.com/%{gh_user}/%{name}
export LDFLAGS="${LDFLAGS} -X main.commit=%{gh_short} -X main.date=$(date -u +%Y%m%d.%H%M%%S) -X main.version=%{version}"

%gobuild -o %{_builddir}/bin/%{name}

%install
install -Dm0755 %{_builddir}/bin/%{name} %{buildroot}%{_bindir}/%{name}

%files
%{_bindir}/%{name}
%doc %{name}-%{version}/LICENSE %{name}-%{version}/*.md

%changelog
* Fri Aug 31 2018 Jamie Curnow <jc@jc21.com> 1.1.0-1
- Initial spec

