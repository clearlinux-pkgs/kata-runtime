#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : kata-runtime
Version  : 20191207
Release  : 75
URL      : https://github.com/kata-containers/runtime/archive/20191207/runtime-20191207.tar.gz
Source0  : https://github.com/kata-containers/runtime/archive/20191207/runtime-20191207.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : Apache-2.0 BSD-2-Clause BSD-3-Clause CC-BY-SA-4.0 ISC MIT MPL-2.0 MPL-2.0-no-copyleft-exception
Requires: kata-runtime-bin = %{version}-%{release}
Requires: kata-runtime-data = %{version}-%{release}
Requires: kata-runtime-libexec = %{version}-%{release}
Requires: kata-runtime-license = %{version}-%{release}
Requires: kata-runtime-services = %{version}-%{release}
BuildRequires : buildreq-golang
Patch1: 0001-Add-Clear-Linux-docker-integration-for-kata-containe.patch
Patch2: 0002-Set-kata-runtime-as-default-runtime-for-cri-o.patch
Patch3: 0003-Allow-extra-docker-opts-as-a-flag-to-dockerd.patch
Patch4: 0004-Enable-static-PIE-build-for-shim.patch
Patch5: 0005-Fix-tty-issue-in-go-1.15.x.patch

%description
This directory and sub directories contain generated code.
The code is generated via go-swagger

%package bin
Summary: bin components for the kata-runtime package.
Group: Binaries
Requires: kata-runtime-data = %{version}-%{release}
Requires: kata-runtime-libexec = %{version}-%{release}
Requires: kata-runtime-license = %{version}-%{release}
Requires: kata-runtime-services = %{version}-%{release}

%description bin
bin components for the kata-runtime package.


%package data
Summary: data components for the kata-runtime package.
Group: Data

%description data
data components for the kata-runtime package.


%package libexec
Summary: libexec components for the kata-runtime package.
Group: Default
Requires: kata-runtime-license = %{version}-%{release}

%description libexec
libexec components for the kata-runtime package.


%package license
Summary: license components for the kata-runtime package.
Group: Default

%description license
license components for the kata-runtime package.


%package services
Summary: services components for the kata-runtime package.
Group: Systemd services

%description services
services components for the kata-runtime package.


%prep
%setup -q -n runtime-20191207
cd %{_builddir}/runtime-20191207
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1

%build
## build_prepend content
export GOPATH="${PWD}/gopath/"
mkdir -p "${GOPATH}/src/github.com/kata-containers/"
ln -sf "${PWD}" "${GOPATH}/src/github.com/kata-containers/runtime"
cd "${GOPATH}/src/github.com/kata-containers/runtime"
## build_prepend end
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1624662199
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
## make_prepend content
export GO111MODULE="auto"
## make_prepend end
make  %{?_smp_mflags}  SKIP_GO_VERSION_CHECK=y QEMUCMD=kata-qemu-lite-system-x86_64 GOFLAGS="-mod=vendor"


%install
export SOURCE_DATE_EPOCH=1624662199
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/kata-runtime
cp %{_builddir}/runtime-20191207/LICENSE %{buildroot}/usr/share/package-licenses/kata-runtime/7df059597099bb7dcf25d2a9aedfaf4465f72d8d
cp %{_builddir}/runtime-20191207/vendor/github.com/BurntSushi/toml/COPYING %{buildroot}/usr/share/package-licenses/kata-runtime/f9cab757896ef6b3570e62b2df7fb63ab1a34b80
cp %{_builddir}/runtime-20191207/vendor/github.com/BurntSushi/toml/cmd/toml-test-decoder/COPYING %{buildroot}/usr/share/package-licenses/kata-runtime/f9cab757896ef6b3570e62b2df7fb63ab1a34b80
cp %{_builddir}/runtime-20191207/vendor/github.com/BurntSushi/toml/cmd/toml-test-encoder/COPYING %{buildroot}/usr/share/package-licenses/kata-runtime/f9cab757896ef6b3570e62b2df7fb63ab1a34b80
cp %{_builddir}/runtime-20191207/vendor/github.com/BurntSushi/toml/cmd/tomlv/COPYING %{buildroot}/usr/share/package-licenses/kata-runtime/f9cab757896ef6b3570e62b2df7fb63ab1a34b80
cp %{_builddir}/runtime-20191207/vendor/github.com/Microsoft/go-winio/LICENSE %{buildroot}/usr/share/package-licenses/kata-runtime/11a8fec351554e8f6c3f4dac5a1f4049dd467ba8
cp %{_builddir}/runtime-20191207/vendor/github.com/Microsoft/go-winio/archive/tar/LICENSE %{buildroot}/usr/share/package-licenses/kata-runtime/7f7a12bcfc16fab2522aa1a562fd3d2aee429d3b
cp %{_builddir}/runtime-20191207/vendor/github.com/Microsoft/hcsshim/LICENSE %{buildroot}/usr/share/package-licenses/kata-runtime/56b820712432e458f05f883566ca8cd85dcdaad5
cp %{_builddir}/runtime-20191207/vendor/github.com/Microsoft/hcsshim/cmd/runhcs/LICENSE %{buildroot}/usr/share/package-licenses/kata-runtime/8ff574408142cd6bbb2a1b83302de24cb7b35e8b
cp %{_builddir}/runtime-20191207/vendor/github.com/Microsoft/hcsshim/pkg/go-runhcs/LICENSE %{buildroot}/usr/share/package-licenses/kata-runtime/7df059597099bb7dcf25d2a9aedfaf4465f72d8d
cp %{_builddir}/runtime-20191207/vendor/github.com/PuerkitoBio/purell/LICENSE %{buildroot}/usr/share/package-licenses/kata-runtime/33cd8e150548e595fbe201c6ca9df582976e71db
cp %{_builddir}/runtime-20191207/vendor/github.com/PuerkitoBio/urlesc/LICENSE %{buildroot}/usr/share/package-licenses/kata-runtime/7f7a12bcfc16fab2522aa1a562fd3d2aee429d3b
cp %{_builddir}/runtime-20191207/vendor/github.com/asaskevich/govalidator/LICENSE %{buildroot}/usr/share/package-licenses/kata-runtime/f0524399083fa802c72bc733a5e12ed1342c650f
cp %{_builddir}/runtime-20191207/vendor/github.com/blang/semver/LICENSE %{buildroot}/usr/share/package-licenses/kata-runtime/16e22f58039363cff486afeac52bde18cd4ab5b3
cp %{_builddir}/runtime-20191207/vendor/github.com/codahale/hdrhistogram/LICENSE %{buildroot}/usr/share/package-licenses/kata-runtime/23d68de7aa2faedcbe131e4ff5b1fdd25af585dd
cp %{_builddir}/runtime-20191207/vendor/github.com/containerd/cgroups/LICENSE %{buildroot}/usr/share/package-licenses/kata-runtime/7df059597099bb7dcf25d2a9aedfaf4465f72d8d
cp %{_builddir}/runtime-20191207/vendor/github.com/containerd/console/LICENSE %{buildroot}/usr/share/package-licenses/kata-runtime/d3b7a70b03b43d4e7205d178100581923a0baad2
cp %{_builddir}/runtime-20191207/vendor/github.com/containerd/containerd/LICENSE %{buildroot}/usr/share/package-licenses/kata-runtime/d3b7a70b03b43d4e7205d178100581923a0baad2
cp %{_builddir}/runtime-20191207/vendor/github.com/containerd/cri-containerd/LICENSE %{buildroot}/usr/share/package-licenses/kata-runtime/92170cdc034b2ff819323ff670d3b7266c8bffcd
cp %{_builddir}/runtime-20191207/vendor/github.com/containerd/fifo/LICENSE %{buildroot}/usr/share/package-licenses/kata-runtime/7df059597099bb7dcf25d2a9aedfaf4465f72d8d
cp %{_builddir}/runtime-20191207/vendor/github.com/containerd/go-runc/LICENSE %{buildroot}/usr/share/package-licenses/kata-runtime/7df059597099bb7dcf25d2a9aedfaf4465f72d8d
cp %{_builddir}/runtime-20191207/vendor/github.com/containerd/ttrpc/LICENSE %{buildroot}/usr/share/package-licenses/kata-runtime/7df059597099bb7dcf25d2a9aedfaf4465f72d8d
cp %{_builddir}/runtime-20191207/vendor/github.com/containerd/typeurl/LICENSE %{buildroot}/usr/share/package-licenses/kata-runtime/d3b7a70b03b43d4e7205d178100581923a0baad2
cp %{_builddir}/runtime-20191207/vendor/github.com/containernetworking/cni/LICENSE %{buildroot}/usr/share/package-licenses/kata-runtime/669a1e53b9dd9df3474300d3d959bb85bad75945
cp %{_builddir}/runtime-20191207/vendor/github.com/containernetworking/plugins/LICENSE %{buildroot}/usr/share/package-licenses/kata-runtime/92170cdc034b2ff819323ff670d3b7266c8bffcd
cp %{_builddir}/runtime-20191207/vendor/github.com/coreos/go-systemd/LICENSE %{buildroot}/usr/share/package-licenses/kata-runtime/172ca3bbafe312a1cf09cfff26953db2f425c28e
cp %{_builddir}/runtime-20191207/vendor/github.com/cri-o/cri-o/LICENSE %{buildroot}/usr/share/package-licenses/kata-runtime/92170cdc034b2ff819323ff670d3b7266c8bffcd
cp %{_builddir}/runtime-20191207/vendor/github.com/davecgh/go-spew/LICENSE %{buildroot}/usr/share/package-licenses/kata-runtime/d2f340a01dd48b589a70f627cf7058c585a315e4
cp %{_builddir}/runtime-20191207/vendor/github.com/dlespiau/covertool/LICENSE %{buildroot}/usr/share/package-licenses/kata-runtime/92170cdc034b2ff819323ff670d3b7266c8bffcd
cp %{_builddir}/runtime-20191207/vendor/github.com/docker/go-units/LICENSE %{buildroot}/usr/share/package-licenses/kata-runtime/3110e55750143a84918d7423febc9c83a55bc28c
cp %{_builddir}/runtime-20191207/vendor/github.com/globalsign/mgo/LICENSE %{buildroot}/usr/share/package-licenses/kata-runtime/9f288d8b22648404d58f00d5e7f6f0d746836182
cp %{_builddir}/runtime-20191207/vendor/github.com/globalsign/mgo/bson/LICENSE %{buildroot}/usr/share/package-licenses/kata-runtime/6b003b30f7a30a203efcf0307e47ea4fca894e6e
cp %{_builddir}/runtime-20191207/vendor/github.com/globalsign/mgo/internal/json/LICENSE %{buildroot}/usr/share/package-licenses/kata-runtime/7f7a12bcfc16fab2522aa1a562fd3d2aee429d3b
cp %{_builddir}/runtime-20191207/vendor/github.com/go-ini/ini/LICENSE %{buildroot}/usr/share/package-licenses/kata-runtime/172ca3bbafe312a1cf09cfff26953db2f425c28e
cp %{_builddir}/runtime-20191207/vendor/github.com/go-openapi/analysis/LICENSE %{buildroot}/usr/share/package-licenses/kata-runtime/2b8b815229aa8a61e483fb4ba0588b8b6c491890
cp %{_builddir}/runtime-20191207/vendor/github.com/go-openapi/errors/LICENSE %{buildroot}/usr/share/package-licenses/kata-runtime/2b8b815229aa8a61e483fb4ba0588b8b6c491890
cp %{_builddir}/runtime-20191207/vendor/github.com/go-openapi/jsonpointer/LICENSE %{buildroot}/usr/share/package-licenses/kata-runtime/2b8b815229aa8a61e483fb4ba0588b8b6c491890
cp %{_builddir}/runtime-20191207/vendor/github.com/go-openapi/jsonreference/LICENSE %{buildroot}/usr/share/package-licenses/kata-runtime/2b8b815229aa8a61e483fb4ba0588b8b6c491890
cp %{_builddir}/runtime-20191207/vendor/github.com/go-openapi/loads/LICENSE %{buildroot}/usr/share/package-licenses/kata-runtime/2b8b815229aa8a61e483fb4ba0588b8b6c491890
cp %{_builddir}/runtime-20191207/vendor/github.com/go-openapi/runtime/LICENSE %{buildroot}/usr/share/package-licenses/kata-runtime/2b8b815229aa8a61e483fb4ba0588b8b6c491890
cp %{_builddir}/runtime-20191207/vendor/github.com/go-openapi/runtime/middleware/denco/LICENSE %{buildroot}/usr/share/package-licenses/kata-runtime/48c378c760084a10ecfdab86c88abf1707b06741
cp %{_builddir}/runtime-20191207/vendor/github.com/go-openapi/spec/LICENSE %{buildroot}/usr/share/package-licenses/kata-runtime/2b8b815229aa8a61e483fb4ba0588b8b6c491890
cp %{_builddir}/runtime-20191207/vendor/github.com/go-openapi/spec/license.go %{buildroot}/usr/share/package-licenses/kata-runtime/555e9ac61d94352b3c2935e77b51fc6dc31d4822
cp %{_builddir}/runtime-20191207/vendor/github.com/go-openapi/strfmt/LICENSE %{buildroot}/usr/share/package-licenses/kata-runtime/2b8b815229aa8a61e483fb4ba0588b8b6c491890
cp %{_builddir}/runtime-20191207/vendor/github.com/go-openapi/swag/LICENSE %{buildroot}/usr/share/package-licenses/kata-runtime/2b8b815229aa8a61e483fb4ba0588b8b6c491890
cp %{_builddir}/runtime-20191207/vendor/github.com/go-openapi/validate/LICENSE %{buildroot}/usr/share/package-licenses/kata-runtime/2b8b815229aa8a61e483fb4ba0588b8b6c491890
cp %{_builddir}/runtime-20191207/vendor/github.com/godbus/dbus/LICENSE %{buildroot}/usr/share/package-licenses/kata-runtime/994658c265db5dbf456fa6163905cc9c0b3bda46
cp %{_builddir}/runtime-20191207/vendor/github.com/gogo/protobuf/LICENSE %{buildroot}/usr/share/package-licenses/kata-runtime/06b27345acae9303e13dde9974d2b2e318b05989
cp %{_builddir}/runtime-20191207/vendor/github.com/golang/protobuf/LICENSE %{buildroot}/usr/share/package-licenses/kata-runtime/aa9b240f558caed367795f667629ccbca28f20b2
cp %{_builddir}/runtime-20191207/vendor/github.com/grpc-ecosystem/grpc-opentracing/LICENSE %{buildroot}/usr/share/package-licenses/kata-runtime/cc9d362955ac00e08a474b658a935cd51da52007
cp %{_builddir}/runtime-20191207/vendor/github.com/hashicorp/errwrap/LICENSE %{buildroot}/usr/share/package-licenses/kata-runtime/523489384296f403da31edf8edf6f9023d328517
cp %{_builddir}/runtime-20191207/vendor/github.com/hashicorp/go-multierror/LICENSE %{buildroot}/usr/share/package-licenses/kata-runtime/2ebe302ef4d8d257ac6f0a916285b51937a25641
cp %{_builddir}/runtime-20191207/vendor/github.com/hashicorp/yamux/LICENSE %{buildroot}/usr/share/package-licenses/kata-runtime/784701375491309231e6d26850c410e36c246d15
cp %{_builddir}/runtime-20191207/vendor/github.com/intel/govmm/COPYING %{buildroot}/usr/share/package-licenses/kata-runtime/2b8b815229aa8a61e483fb4ba0588b8b6c491890
cp %{_builddir}/runtime-20191207/vendor/github.com/kata-containers/agent/LICENSE %{buildroot}/usr/share/package-licenses/kata-runtime/7df059597099bb7dcf25d2a9aedfaf4465f72d8d
cp %{_builddir}/runtime-20191207/vendor/github.com/mailru/easyjson/LICENSE %{buildroot}/usr/share/package-licenses/kata-runtime/554fb441fbb1607579b7c9f8e9d7fab5d00e3a51
cp %{_builddir}/runtime-20191207/vendor/github.com/mdlayher/vsock/LICENSE.md %{buildroot}/usr/share/package-licenses/kata-runtime/a399653ce1cf03767aa146924f33db27bfdd16ac
cp %{_builddir}/runtime-20191207/vendor/github.com/mitchellh/mapstructure/LICENSE %{buildroot}/usr/share/package-licenses/kata-runtime/5ad2002bc8d2b22e2034867d159f71ba6258e18f
cp %{_builddir}/runtime-20191207/vendor/github.com/opencontainers/go-digest/LICENSE.code %{buildroot}/usr/share/package-licenses/kata-runtime/76a37a42a06aa6e231383fb93d9161f074d5962b
cp %{_builddir}/runtime-20191207/vendor/github.com/opencontainers/go-digest/LICENSE.docs %{buildroot}/usr/share/package-licenses/kata-runtime/979fd7d5c67073b265d96f584aac3de1c419b8e2
cp %{_builddir}/runtime-20191207/vendor/github.com/opencontainers/runc/LICENSE %{buildroot}/usr/share/package-licenses/kata-runtime/8ff574408142cd6bbb2a1b83302de24cb7b35e8b
cp %{_builddir}/runtime-20191207/vendor/github.com/opencontainers/runtime-spec/LICENSE %{buildroot}/usr/share/package-licenses/kata-runtime/552b909d29bd260c886142a969b462c85f976dcd
cp %{_builddir}/runtime-20191207/vendor/github.com/opentracing/opentracing-go/LICENSE %{buildroot}/usr/share/package-licenses/kata-runtime/75b05723a69674cde02ec34aac00db38fbbabccd
cp %{_builddir}/runtime-20191207/vendor/github.com/pkg/errors/LICENSE %{buildroot}/usr/share/package-licenses/kata-runtime/9c1bedc0d42f24c24a1bd266f3ce101a4b0579fc
cp %{_builddir}/runtime-20191207/vendor/github.com/pmezard/go-difflib/LICENSE %{buildroot}/usr/share/package-licenses/kata-runtime/cd3e4d932cee20da681e6b3bee8139cb4f734034
cp %{_builddir}/runtime-20191207/vendor/github.com/prometheus/procfs/LICENSE %{buildroot}/usr/share/package-licenses/kata-runtime/7df059597099bb7dcf25d2a9aedfaf4465f72d8d
cp %{_builddir}/runtime-20191207/vendor/github.com/safchain/ethtool/LICENSE %{buildroot}/usr/share/package-licenses/kata-runtime/669a1e53b9dd9df3474300d3d959bb85bad75945
cp %{_builddir}/runtime-20191207/vendor/github.com/seccomp/libseccomp-golang/LICENSE %{buildroot}/usr/share/package-licenses/kata-runtime/cd87737b0bbdeee650f6a72ee61209863b1d827f
cp %{_builddir}/runtime-20191207/vendor/github.com/sirupsen/logrus/LICENSE %{buildroot}/usr/share/package-licenses/kata-runtime/a1c7852c717fed2c9a0284ed112ea66013230da6
cp %{_builddir}/runtime-20191207/vendor/github.com/stretchr/testify/LICENCE.txt %{buildroot}/usr/share/package-licenses/kata-runtime/5e630aeef4ff3e9b29a46622496b3fbbf5d7fe56
cp %{_builddir}/runtime-20191207/vendor/github.com/stretchr/testify/LICENSE %{buildroot}/usr/share/package-licenses/kata-runtime/5e630aeef4ff3e9b29a46622496b3fbbf5d7fe56
cp %{_builddir}/runtime-20191207/vendor/github.com/uber/jaeger-client-go/LICENSE %{buildroot}/usr/share/package-licenses/kata-runtime/7df059597099bb7dcf25d2a9aedfaf4465f72d8d
cp %{_builddir}/runtime-20191207/vendor/github.com/uber/jaeger-lib/LICENSE %{buildroot}/usr/share/package-licenses/kata-runtime/7df059597099bb7dcf25d2a9aedfaf4465f72d8d
cp %{_builddir}/runtime-20191207/vendor/github.com/urfave/cli/LICENSE %{buildroot}/usr/share/package-licenses/kata-runtime/62e85c543bad57a03eff756c0cfcb4bd26b77a4a
cp %{_builddir}/runtime-20191207/vendor/github.com/vishvananda/netlink/LICENSE %{buildroot}/usr/share/package-licenses/kata-runtime/f88291c879c4ee329bfa341b54eaedd29d3058cf
cp %{_builddir}/runtime-20191207/vendor/github.com/vishvananda/netns/LICENSE %{buildroot}/usr/share/package-licenses/kata-runtime/f88291c879c4ee329bfa341b54eaedd29d3058cf
cp %{_builddir}/runtime-20191207/vendor/golang.org/x/crypto/LICENSE %{buildroot}/usr/share/package-licenses/kata-runtime/d6a5f1ecaedd723c325a2063375b3517e808a2b5
cp %{_builddir}/runtime-20191207/vendor/golang.org/x/net/LICENSE %{buildroot}/usr/share/package-licenses/kata-runtime/d6a5f1ecaedd723c325a2063375b3517e808a2b5
cp %{_builddir}/runtime-20191207/vendor/golang.org/x/oauth2/LICENSE %{buildroot}/usr/share/package-licenses/kata-runtime/d6a5f1ecaedd723c325a2063375b3517e808a2b5
cp %{_builddir}/runtime-20191207/vendor/golang.org/x/sys/LICENSE %{buildroot}/usr/share/package-licenses/kata-runtime/d6a5f1ecaedd723c325a2063375b3517e808a2b5
cp %{_builddir}/runtime-20191207/vendor/golang.org/x/text/LICENSE %{buildroot}/usr/share/package-licenses/kata-runtime/d6a5f1ecaedd723c325a2063375b3517e808a2b5
cp %{_builddir}/runtime-20191207/vendor/google.golang.org/appengine/LICENSE %{buildroot}/usr/share/package-licenses/kata-runtime/2b8b815229aa8a61e483fb4ba0588b8b6c491890
cp %{_builddir}/runtime-20191207/vendor/google.golang.org/genproto/LICENSE %{buildroot}/usr/share/package-licenses/kata-runtime/2b8b815229aa8a61e483fb4ba0588b8b6c491890
cp %{_builddir}/runtime-20191207/vendor/google.golang.org/grpc/LICENSE %{buildroot}/usr/share/package-licenses/kata-runtime/2b8b815229aa8a61e483fb4ba0588b8b6c491890
cp %{_builddir}/runtime-20191207/vendor/gopkg.in/yaml.v2/LICENSE %{buildroot}/usr/share/package-licenses/kata-runtime/92170cdc034b2ff819323ff670d3b7266c8bffcd
cp %{_builddir}/runtime-20191207/vendor/gopkg.in/yaml.v2/LICENSE.libyaml %{buildroot}/usr/share/package-licenses/kata-runtime/ad00ce7340d89dc13ccc59920ef75cb55af5b164
cp %{_builddir}/runtime-20191207/vendor/gopkg.in/yaml.v2/NOTICE %{buildroot}/usr/share/package-licenses/kata-runtime/9522d95b2b9b284285cc3fb6ecc445aa3ee5e785
cp %{_builddir}/runtime-20191207/virtcontainers/LICENSE %{buildroot}/usr/share/package-licenses/kata-runtime/92170cdc034b2ff819323ff670d3b7266c8bffcd
cp %{_builddir}/runtime-20191207/virtcontainers/pkg/oci/LICENSE %{buildroot}/usr/share/package-licenses/kata-runtime/92170cdc034b2ff819323ff670d3b7266c8bffcd
%make_install SKIP_GO_VERSION_CHECK=y GOPATH="${PWD}/gopath/" PREFIX=/usr/
## install_append content
sed -i -e '/^initrd =/d' %{buildroot}/usr/share/defaults/kata-containers/configuration-qemu.toml
install -m 0644 -D clearlinux.conf %{buildroot}/usr/lib/systemd/system/docker.service.d/clearlinux.conf
install -m 0644 -D 50-runtime.conf %{buildroot}/usr/lib/systemd/system/docker.service.d/50-runtime.conf

install -m 0755 -D set-crio-default-runtime %{buildroot}/usr/bin/set-crio-default-runtime
install -m 0644 -D crio-clearlinux.conf %{buildroot}/usr/lib/systemd/system/crio.service.d/crio-clearlinux.conf
install -m 0644 -D crio-set-runtime.service %{buildroot}/usr/lib/systemd/system/crio-set-runtime.service
## install_append end

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/containerd-shim-kata-v2
/usr/bin/kata-collect-data.sh
/usr/bin/kata-runtime
/usr/bin/set-crio-default-runtime

%files data
%defattr(-,root,root,-)
/usr/share/bash-completion/completions/kata-runtime
/usr/share/defaults/kata-containers/configuration-acrn.toml
/usr/share/defaults/kata-containers/configuration-clh.toml
/usr/share/defaults/kata-containers/configuration-fc.toml
/usr/share/defaults/kata-containers/configuration-qemu-virtiofs.toml
/usr/share/defaults/kata-containers/configuration-qemu.toml
/usr/share/defaults/kata-containers/configuration.toml

%files libexec
%defattr(-,root,root,-)
/usr/libexec/kata-containers/kata-netmon

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/kata-runtime/06b27345acae9303e13dde9974d2b2e318b05989
/usr/share/package-licenses/kata-runtime/11a8fec351554e8f6c3f4dac5a1f4049dd467ba8
/usr/share/package-licenses/kata-runtime/16e22f58039363cff486afeac52bde18cd4ab5b3
/usr/share/package-licenses/kata-runtime/172ca3bbafe312a1cf09cfff26953db2f425c28e
/usr/share/package-licenses/kata-runtime/23d68de7aa2faedcbe131e4ff5b1fdd25af585dd
/usr/share/package-licenses/kata-runtime/2b8b815229aa8a61e483fb4ba0588b8b6c491890
/usr/share/package-licenses/kata-runtime/2ebe302ef4d8d257ac6f0a916285b51937a25641
/usr/share/package-licenses/kata-runtime/3110e55750143a84918d7423febc9c83a55bc28c
/usr/share/package-licenses/kata-runtime/33cd8e150548e595fbe201c6ca9df582976e71db
/usr/share/package-licenses/kata-runtime/48c378c760084a10ecfdab86c88abf1707b06741
/usr/share/package-licenses/kata-runtime/523489384296f403da31edf8edf6f9023d328517
/usr/share/package-licenses/kata-runtime/552b909d29bd260c886142a969b462c85f976dcd
/usr/share/package-licenses/kata-runtime/554fb441fbb1607579b7c9f8e9d7fab5d00e3a51
/usr/share/package-licenses/kata-runtime/555e9ac61d94352b3c2935e77b51fc6dc31d4822
/usr/share/package-licenses/kata-runtime/56b820712432e458f05f883566ca8cd85dcdaad5
/usr/share/package-licenses/kata-runtime/5ad2002bc8d2b22e2034867d159f71ba6258e18f
/usr/share/package-licenses/kata-runtime/5e630aeef4ff3e9b29a46622496b3fbbf5d7fe56
/usr/share/package-licenses/kata-runtime/62e85c543bad57a03eff756c0cfcb4bd26b77a4a
/usr/share/package-licenses/kata-runtime/669a1e53b9dd9df3474300d3d959bb85bad75945
/usr/share/package-licenses/kata-runtime/6b003b30f7a30a203efcf0307e47ea4fca894e6e
/usr/share/package-licenses/kata-runtime/75b05723a69674cde02ec34aac00db38fbbabccd
/usr/share/package-licenses/kata-runtime/76a37a42a06aa6e231383fb93d9161f074d5962b
/usr/share/package-licenses/kata-runtime/784701375491309231e6d26850c410e36c246d15
/usr/share/package-licenses/kata-runtime/7df059597099bb7dcf25d2a9aedfaf4465f72d8d
/usr/share/package-licenses/kata-runtime/7f7a12bcfc16fab2522aa1a562fd3d2aee429d3b
/usr/share/package-licenses/kata-runtime/8ff574408142cd6bbb2a1b83302de24cb7b35e8b
/usr/share/package-licenses/kata-runtime/92170cdc034b2ff819323ff670d3b7266c8bffcd
/usr/share/package-licenses/kata-runtime/9522d95b2b9b284285cc3fb6ecc445aa3ee5e785
/usr/share/package-licenses/kata-runtime/979fd7d5c67073b265d96f584aac3de1c419b8e2
/usr/share/package-licenses/kata-runtime/994658c265db5dbf456fa6163905cc9c0b3bda46
/usr/share/package-licenses/kata-runtime/9c1bedc0d42f24c24a1bd266f3ce101a4b0579fc
/usr/share/package-licenses/kata-runtime/9f288d8b22648404d58f00d5e7f6f0d746836182
/usr/share/package-licenses/kata-runtime/a1c7852c717fed2c9a0284ed112ea66013230da6
/usr/share/package-licenses/kata-runtime/a399653ce1cf03767aa146924f33db27bfdd16ac
/usr/share/package-licenses/kata-runtime/aa9b240f558caed367795f667629ccbca28f20b2
/usr/share/package-licenses/kata-runtime/ad00ce7340d89dc13ccc59920ef75cb55af5b164
/usr/share/package-licenses/kata-runtime/cc9d362955ac00e08a474b658a935cd51da52007
/usr/share/package-licenses/kata-runtime/cd3e4d932cee20da681e6b3bee8139cb4f734034
/usr/share/package-licenses/kata-runtime/cd87737b0bbdeee650f6a72ee61209863b1d827f
/usr/share/package-licenses/kata-runtime/d2f340a01dd48b589a70f627cf7058c585a315e4
/usr/share/package-licenses/kata-runtime/d3b7a70b03b43d4e7205d178100581923a0baad2
/usr/share/package-licenses/kata-runtime/d6a5f1ecaedd723c325a2063375b3517e808a2b5
/usr/share/package-licenses/kata-runtime/f0524399083fa802c72bc733a5e12ed1342c650f
/usr/share/package-licenses/kata-runtime/f88291c879c4ee329bfa341b54eaedd29d3058cf
/usr/share/package-licenses/kata-runtime/f9cab757896ef6b3570e62b2df7fb63ab1a34b80

%files services
%defattr(-,root,root,-)
/usr/lib/systemd/system/crio-set-runtime.service
/usr/lib/systemd/system/crio.service.d/crio-clearlinux.conf
/usr/lib/systemd/system/docker.service.d/50-runtime.conf
/usr/lib/systemd/system/docker.service.d/clearlinux.conf
