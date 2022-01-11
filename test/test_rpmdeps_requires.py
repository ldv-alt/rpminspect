#
# Copyright © 2021 Red Hat, Inc.
# Author(s): David Cantrell <dcantrell@redhat.com>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
#

from rpmfluff.sourcefile import SourceFile
from rpmfluff.samples import hello_world
from rpmfluff.utils import CC

from baseclass import TestKoji, TestRPMs, TestSRPM
from baseclass import TestCompareKoji, TestCompareRPMs, TestCompareSRPM
from baseclass import BEFORE_NAME, BEFORE_VER, BEFORE_REL
from baseclass import AFTER_NAME, AFTER_VER, AFTER_REL

before_requires = "important-package >= 2.0.2-47"
after_requires = "important-package >= 4.7.0-1"
unexpanded_requires = "important-package >= 4.7.1-1%{_macro}"


# Requires dependency is correct (OK) - control case
class RequiresCorrectSRPM(TestSRPM):
    def setUp(self):
        super().setUp()

        self.rpm.add_build_requires(after_requires)

        self.inspection = "rpmdeps"
        self.result = "OK"
        self.waiver_auth = "Not Waivable"


class RequiresCorrectRPMs(TestRPMs):
    def setUp(self):
        super().setUp()

        self.rpm.add_requires(after_requires)

        self.inspection = "rpmdeps"
        self.result = "OK"
        self.waiver_auth = "Not Waivable"


class RequiresCorrectKoji(TestKoji):
    def setUp(self):
        super().setUp()

        self.rpm.add_requires(after_requires)

        self.inspection = "rpmdeps"
        self.result = "OK"
        self.waiver_auth = "Not Waivable"


# Retaining Requires dependency in rebase comparison (INFO)
class RetainingRequiresRebaseCompareSRPM(TestCompareSRPM):
    def setUp(self):
        super().setUp(rebase=True)

        self.before_rpm.add_build_requires(after_requires)
        self.after_rpm.add_build_requires(after_requires)

        self.inspection = "rpmdeps"
        self.result = "INFO"
        self.waiver_auth = "Not Waivable"


class RetainingRequiresRebaseCompareRPMs(TestCompareRPMs):
    def setUp(self):
        super().setUp(rebase=True)

        self.before_rpm.add_requires(after_requires)
        self.after_rpm.add_requires(after_requires)

        self.inspection = "rpmdeps"
        self.result = "INFO"
        self.waiver_auth = "Not Waivable"


class RetainingRequiresRebaseCompareKoji(TestCompareKoji):
    def setUp(self):
        super().setUp(rebase=True)

        self.before_rpm.add_requires(after_requires)
        self.after_rpm.add_requires(after_requires)

        self.inspection = "rpmdeps"
        self.result = "INFO"
        self.waiver_auth = "Not Waivable"


# Retaining Requires dependency in maint comparison (OK)
class RetainingRequiresCompareSRPM(TestCompareSRPM):
    def setUp(self):
        super().setUp()

        self.before_rpm.add_build_requires(after_requires)
        self.after_rpm.add_build_requires(after_requires)

        self.inspection = "rpmdeps"
        self.result = "OK"
        self.waiver_auth = "Not Waivable"


class RetainingRequiresCompareRPMs(TestCompareRPMs):
    def setUp(self):
        super().setUp()

        self.before_rpm.add_requires(after_requires)
        self.after_rpm.add_requires(after_requires)

        self.inspection = "rpmdeps"
        self.result = "OK"
        self.waiver_auth = "Not Waivable"


class RetainingRequiresCompareKoji(TestCompareKoji):
    def setUp(self):
        super().setUp()

        self.before_rpm.add_requires(after_requires)
        self.after_rpm.add_requires(after_requires)

        self.inspection = "rpmdeps"
        self.result = "OK"
        self.waiver_auth = "Not Waivable"


# Gaining a new Requires in a rebase comparison (INFO)
class GainingRequiresRebaseCompareSRPM(TestCompareSRPM):
    def setUp(self):
        super().setUp(rebase=True)

        self.after_rpm.add_build_requires(after_requires)

        self.inspection = "rpmdeps"
        self.result = "INFO"
        self.waiver_auth = "Not Waivable"


class GainingRequiresRebaseCompareRPMs(TestCompareRPMs):
    def setUp(self):
        super().setUp(rebase=True)

        self.after_rpm.add_requires(after_requires)

        self.inspection = "rpmdeps"
        self.result = "INFO"
        self.waiver_auth = "Not Waivable"


class GainingRequiresRebaseCompareKoji(TestCompareKoji):
    def setUp(self):
        super().setUp(rebase=True)

        self.after_rpm.add_requires(after_requires)

        self.inspection = "rpmdeps"
        self.result = "INFO"
        self.waiver_auth = "Not Waivable"


# Gaining a new Requires in a maint comparison (VERIFY)
class GainingRequiresCompareSRPM(TestCompareSRPM):
    def setUp(self):
        super().setUp()

        self.after_rpm.add_build_requires(after_requires)

        self.inspection = "rpmdeps"
        self.result = "VERIFY"
        self.waiver_auth = "Anyone"


class GainingRequiresCompareRPMs(TestCompareRPMs):
    def setUp(self):
        super().setUp()

        self.after_rpm.add_requires(after_requires)

        self.inspection = "rpmdeps"
        self.result = "VERIFY"
        self.waiver_auth = "Anyone"


class GainingRequiresCompareKoji(TestCompareKoji):
    def setUp(self):
        super().setUp()

        self.after_rpm.add_requires(after_requires)

        self.inspection = "rpmdeps"
        self.result = "VERIFY"
        self.waiver_auth = "Anyone"


# Changing a Requires in a rebase comparison (INFO)
class ChangingRequiresRebaseCompareSRPM(TestCompareSRPM):
    def setUp(self):
        super().setUp(rebase=True)

        self.before_rpm.add_build_requires(before_requires)
        self.after_rpm.add_build_requires(after_requires)

        self.inspection = "rpmdeps"
        self.result = "INFO"
        self.waiver_auth = "Not Waivable"


class ChangingRequiresRebaseCompareRPMs(TestCompareRPMs):
    def setUp(self):
        super().setUp(rebase=True)

        self.before_rpm.add_requires(before_requires)
        self.after_rpm.add_requires(after_requires)

        self.inspection = "rpmdeps"
        self.result = "INFO"
        self.waiver_auth = "Not Waivable"


class ChangingRequiresRebaseCompareKoji(TestCompareKoji):
    def setUp(self):
        super().setUp(rebase=True)

        self.before_rpm.add_requires(before_requires)
        self.after_rpm.add_requires(after_requires)

        self.inspection = "rpmdeps"
        self.result = "INFO"
        self.waiver_auth = "Not Waivable"


# Changing a Requires in a maint comparison (VERIFY)
class ChangingRequiresCompareSRPM(TestCompareSRPM):
    def setUp(self):
        super().setUp()

        self.before_rpm.add_build_requires(before_requires)
        self.after_rpm.add_build_requires(after_requires)

        self.inspection = "rpmdeps"
        # only INFO level because it's the SRPM
        self.result = "INFO"
        self.waiver_auth = "Not Waivable"


class ChangingRequiresCompareRPMs(TestCompareRPMs):
    def setUp(self):
        super().setUp()

        self.before_rpm.add_requires(before_requires)
        self.after_rpm.add_requires(after_requires)

        self.inspection = "rpmdeps"
        self.result = "VERIFY"
        self.waiver_auth = "Anyone"


class ChangingRequiresCompareKoji(TestCompareKoji):
    def setUp(self):
        super().setUp()

        self.before_rpm.add_requires(before_requires)
        self.after_rpm.add_requires(after_requires)

        self.inspection = "rpmdeps"
        self.result = "VERIFY"
        self.waiver_auth = "Anyone"


# Changing a Requires in a maint comparison due to NVR (INFO)
class ChangingRequiresExpectedCompareSRPM(TestCompareSRPM):
    def setUp(self):
        super().setUp()

        self.inspection = "rpmdeps"
        self.result = "INFO"
        self.waiver_auth = "Not Waivable"


class ChangingRequiresExpectedCompareRPMs(TestCompareRPMs):
    def setUp(self):
        super().setUp()

        self.inspection = "rpmdeps"
        self.result = "INFO"
        self.waiver_auth = "Not Waivable"


class ChangingRequiresExpectedCompareKoji(TestCompareKoji):
    def setUp(self):
        super().setUp()

        self.inspection = "rpmdeps"
        self.result = "INFO"
        self.waiver_auth = "Not Waivable"


# Losing a Requires in a rebase comparison (INFO)
class LosingRequiresRebaseCompareSRPM(TestCompareSRPM):
    def setUp(self):
        super().setUp(rebase=True)

        self.before_rpm.add_build_requires(before_requires)

        self.inspection = "rpmdeps"
        self.result = "INFO"
        self.waiver_auth = "Not Waivable"


class LosingRequiresRebaseCompareRPMs(TestCompareRPMs):
    def setUp(self):
        super().setUp(rebase=True)

        self.before_rpm.add_requires(before_requires)

        self.inspection = "rpmdeps"
        self.result = "INFO"
        self.waiver_auth = "Not Waivable"


class LosingRequiresRebaseCompareKoji(TestCompareKoji):
    def setUp(self):
        super().setUp(rebase=True)

        self.before_rpm.add_requires(before_requires)

        self.inspection = "rpmdeps"
        self.result = "INFO"
        self.waiver_auth = "Not Waivable"


# Losing a Requires in a maint comparison (VERIFY)
class LosingRequiresCompareSRPM(TestCompareSRPM):
    def setUp(self):
        super().setUp()

        self.before_rpm.add_build_requires(before_requires)

        self.inspection = "rpmdeps"
        self.result = "VERIFY"
        self.waiver_auth = "Anyone"


class LosingRequiresCompareRPMs(TestCompareRPMs):
    def setUp(self):
        super().setUp()

        self.before_rpm.add_requires(before_requires)

        self.inspection = "rpmdeps"
        self.result = "VERIFY"
        self.waiver_auth = "Anyone"


class LosingRequiresCompareKoji(TestCompareKoji):
    def setUp(self):
        super().setUp()

        self.before_rpm.add_requires(before_requires)

        self.inspection = "rpmdeps"
        self.result = "VERIFY"
        self.waiver_auth = "Anyone"


# Missing Epoch prefix on maint compare (BAD for Koji compares, OK
# otherwise)
class MissingEpochRequiresSRPM(TestSRPM):
    def setUp(self):
        super().setUp()

        # define an epoch value
        self.rpm.epoch = 47

        # add a subpackage
        sub = self.rpm.add_subpackage("devel")
        sub.group = "Development/Libraries"

        # we need some stuff in the packages
        self.rpm.add_simple_compilation(installPath="usr/bin/vaporware")
        self.rpm.add_simple_library(
            installPath="usr/lib/libvaporware.so.1", subpackageSuffix="devel"
        )

        # manually add a devel subpackage with an incorrect Requires
        sub.add_requires("%s = %s-%s" % (AFTER_NAME, AFTER_VER, AFTER_REL))

        # the result is OK here because the Epoch check is a no-op for SRPMs
        self.inspection = "rpmdeps"
        self.result = "OK"
        self.waiver_auth = "Not Waivable"


class MissingEpochRequiresRPMs(TestRPMs):
    def setUp(self):
        super().setUp()

        # define an epoch value
        self.rpm.epoch = 47

        # add a subpackage
        sub = self.rpm.add_subpackage("devel")
        sub.group = "Development/Libraries"

        # we need some stuff in the packages
        self.rpm.add_simple_compilation(installPath="usr/bin/vaporware")
        self.rpm.add_simple_library(
            installPath="usr/lib/libvaporware.so.1", subpackageSuffix="devel"
        )

        # manually add a devel subpackage with an incorrect Requires
        sub.add_requires("%s = %s-%s" % (AFTER_NAME, AFTER_VER, AFTER_REL))

        # the result is OK here because the rpmdeps inspection when
        # run against just a pair of RPMs can't check for missing
        # Epoch values in manual dependencies, so the inspection
        # doesn't fail
        self.inspection = "rpmdeps"
        self.result = "OK"
        self.waiver_auth = "Not Waivable"


class MissingEpochRequiresKoji(TestKoji):
    def setUp(self):
        super().setUp()

        # define an epoch value
        self.rpm.epoch = 47

        # add a subpackage
        sub = self.rpm.add_subpackage("devel")
        sub.group = "Development/Libraries"

        # we need some stuff in the packages
        self.rpm.add_simple_compilation(installPath="usr/bin/vaporware")
        self.rpm.add_simple_library(
            installPath="usr/lib/libvaporware.so.1", subpackageSuffix="devel"
        )

        # manually add a devel subpackage with an incorrect Requires
        sub.add_requires("%s = %s-%s" % (AFTER_NAME, AFTER_VER, AFTER_REL))

        self.inspection = "rpmdeps"
        self.result = "BAD"
        self.waiver_auth = "Anyone"


class MissingEpochRequiresCompareSRPM(TestCompareSRPM):
    def setUp(self):
        super().setUp()

        # define an epoch value
        self.before_rpm.epoch = 47
        self.after_rpm.epoch = 47

        # add a subpackage
        before_sub = self.before_rpm.add_subpackage("devel")
        before_sub.group = "Development/Libraries"
        after_sub = self.after_rpm.add_subpackage("devel")
        after_sub.group = "Development/Libraries"

        # we need some stuff in the packages
        self.before_rpm.add_simple_compilation(installPath="usr/bin/vaporware")
        self.after_rpm.add_simple_compilation(installPath="usr/bin/vaporware")
        self.before_rpm.add_simple_library(
            installPath="usr/lib/libvaporware.so.1", subpackageSuffix="devel"
        )
        self.after_rpm.add_simple_library(
            installPath="usr/lib/libvaporware.so.1", subpackageSuffix="devel"
        )

        # manually add a devel subpackage with an incorrect Requires
        before_sub.add_requires("%s = %s-%s" % (BEFORE_NAME, BEFORE_VER, BEFORE_REL))
        after_sub.add_requires("%s = %s-%s" % (AFTER_NAME, AFTER_VER, AFTER_REL))

        # this is 'OK' because the missing Epoch check is a no-op for SRPMs
        self.inspection = "rpmdeps"
        self.result = "OK"
        self.waiver_auth = "Not Waivable"


class MissingEpochRequiresCompareRPMs(TestCompareRPMs):
    def setUp(self):
        super().setUp()

        # define an epoch value
        self.before_rpm.epoch = 47
        self.after_rpm.epoch = 47

        # add a subpackage
        before_sub = self.before_rpm.add_subpackage("devel")
        before_sub.group = "Development/Libraries"
        after_sub = self.after_rpm.add_subpackage("devel")
        after_sub.group = "Development/Libraries"

        # we need some stuff in the packages
        self.before_rpm.add_simple_compilation(installPath="usr/bin/vaporware")
        self.after_rpm.add_simple_compilation(installPath="usr/bin/vaporware")
        self.before_rpm.add_simple_library(
            installPath="usr/lib/libvaporware.so.1", subpackageSuffix="devel"
        )
        self.after_rpm.add_simple_library(
            installPath="usr/lib/libvaporware.so.1", subpackageSuffix="devel"
        )

        # manually add a devel subpackage with an incorrect Requires
        before_sub.add_requires("%s = %s-%s" % (BEFORE_NAME, BEFORE_VER, BEFORE_REL))
        after_sub.add_requires("%s = %s-%s" % (AFTER_NAME, AFTER_VER, AFTER_REL))

        # this is 'OK' because the Compare RPMs tests don't work with the
        # entire collection of RPMs, it does it iteratively
        self.inspection = "rpmdeps"
        self.result = "OK"
        self.waiver_auth = "Not Waivable"


class MissingEpochRequiresCompareKoji(TestCompareKoji):
    def setUp(self):
        super().setUp()

        # define an epoch value
        self.before_rpm.epoch = 47
        self.after_rpm.epoch = 47

        # add a subpackage
        before_sub = self.before_rpm.add_subpackage("devel")
        before_sub.group = "Development/Libraries"
        after_sub = self.after_rpm.add_subpackage("devel")
        after_sub.group = "Development/Libraries"

        # we need some stuff in the packages
        self.before_rpm.add_simple_compilation(installPath="usr/bin/vaporware")
        self.after_rpm.add_simple_compilation(installPath="usr/bin/vaporware")
        self.before_rpm.add_simple_library(
            installPath="usr/lib/libvaporware.so.1", subpackageSuffix="devel"
        )
        self.after_rpm.add_simple_library(
            installPath="usr/lib/libvaporware.so.1", subpackageSuffix="devel"
        )

        # manually add a devel subpackage with an incorrect Requires
        before_sub.add_requires("%s = %s-%s" % (BEFORE_NAME, BEFORE_VER, BEFORE_REL))
        after_sub.add_requires("%s = %s-%s" % (AFTER_NAME, AFTER_VER, AFTER_REL))

        self.inspection = "rpmdeps"
        self.result = "BAD"
        self.waiver_auth = "Anyone"


# Missing Epoch prefix on rebase compare (INFO)
class MissingEpochRequiresRebaseCompareSRPM(TestCompareSRPM):
    def setUp(self):
        super().setUp(rebase=True)

        # define an epoch value
        self.before_rpm.epoch = 47
        self.after_rpm.epoch = 47

        # add a subpackage
        before_sub = self.before_rpm.add_subpackage("devel")
        before_sub.group = "Development/Libraries"
        after_sub = self.after_rpm.add_subpackage("devel")
        after_sub.group = "Development/Libraries"

        # we need some stuff in the packages
        self.before_rpm.add_simple_compilation(installPath="usr/bin/vaporware")
        self.after_rpm.add_simple_compilation(installPath="usr/bin/vaporware")
        self.before_rpm.add_simple_library(
            installPath="usr/lib/libvaporware.so.1", subpackageSuffix="devel"
        )
        self.after_rpm.add_simple_library(
            installPath="usr/lib/libvaporware.so.1", subpackageSuffix="devel"
        )

        # manually add a devel subpackage with an incorrect Requires
        before_sub.add_requires("%s = %s-%s" % (BEFORE_NAME, BEFORE_VER, BEFORE_REL))
        after_sub.add_requires("%s = %s-%s" % (AFTER_NAME, AFTER_VER, AFTER_REL))

        self.inspection = "rpmdeps"
        self.result = "INFO"
        self.waiver_auth = "Not Waivable"


class MissingEpochRequiresRebaseCompareRPMs(TestCompareRPMs):
    def setUp(self):
        super().setUp(rebase=True)

        # define an epoch value
        self.before_rpm.epoch = 47
        self.after_rpm.epoch = 47

        # add a subpackage
        before_sub = self.before_rpm.add_subpackage("devel")
        before_sub.group = "Development/Libraries"
        after_sub = self.after_rpm.add_subpackage("devel")
        after_sub.group = "Development/Libraries"

        # we need some stuff in the packages
        self.before_rpm.add_simple_compilation(installPath="usr/bin/vaporware")
        self.after_rpm.add_simple_compilation(installPath="usr/bin/vaporware")
        self.before_rpm.add_simple_library(
            installPath="usr/lib/libvaporware.so.1", subpackageSuffix="devel"
        )
        self.after_rpm.add_simple_library(
            installPath="usr/lib/libvaporware.so.1", subpackageSuffix="devel"
        )

        # manually add a devel subpackage with an incorrect Requires
        before_sub.add_requires("%s = %s-%s" % (BEFORE_NAME, BEFORE_VER, BEFORE_REL))
        after_sub.add_requires("%s = %s-%s" % (AFTER_NAME, AFTER_VER, AFTER_REL))

        self.inspection = "rpmdeps"
        self.result = "INFO"
        self.waiver_auth = "Not Waivable"


class MissingEpochRequiresRebaseCompareKoji(TestCompareKoji):
    def setUp(self):
        super().setUp(rebase=True)

        # define an epoch value
        self.before_rpm.epoch = 47
        self.after_rpm.epoch = 47

        # add a subpackage
        before_sub = self.before_rpm.add_subpackage("devel")
        before_sub.group = "Development/Libraries"
        after_sub = self.after_rpm.add_subpackage("devel")
        after_sub.group = "Development/Libraries"

        # we need some stuff in the packages
        self.before_rpm.add_simple_compilation(installPath="usr/bin/vaporware")
        self.after_rpm.add_simple_compilation(installPath="usr/bin/vaporware")
        self.before_rpm.add_simple_library(
            installPath="usr/lib/libvaporware.so.1", subpackageSuffix="devel"
        )
        self.after_rpm.add_simple_library(
            installPath="usr/lib/libvaporware.so.1", subpackageSuffix="devel"
        )

        # manually add a devel subpackage with an incorrect Requires
        before_sub.add_requires("%s = %s-%s" % (BEFORE_NAME, BEFORE_VER, BEFORE_REL))
        after_sub.add_requires("%s = %s-%s" % (AFTER_NAME, AFTER_VER, AFTER_REL))

        self.inspection = "rpmdeps"
        self.result = "INFO"
        self.waiver_auth = "Not Waivable"


# Unexpanded macro in Requires (BAD)
class UnexpandedMacroRequiresSRPM(TestSRPM):
    def setUp(self):
        super().setUp()

        self.rpm.add_requires(unexpanded_requires)

        # this is OK because it's the SRPM
        self.inspection = "rpmdeps"
        self.result = "OK"
        self.waiver_auth = "Not Waivable"


class UnexpandedMacroRequiresRPMs(TestRPMs):
    def setUp(self):
        super().setUp()

        self.rpm.add_requires(unexpanded_requires)

        self.inspection = "rpmdeps"
        self.result = "BAD"
        self.waiver_auth = "Anyone"


class UnexpandedMacroRequiresKoji(TestKoji):
    def setUp(self):
        super().setUp()

        self.rpm.add_requires(unexpanded_requires)

        self.inspection = "rpmdeps"
        self.result = "BAD"
        self.waiver_auth = "Anyone"


class UnexpandedMacroRequiresCompareSRPM(TestCompareSRPM):
    def setUp(self):
        super().setUp()

        self.before_rpm.add_requires(unexpanded_requires)
        self.after_rpm.add_requires(unexpanded_requires)

        # this is OK because it's the SRPM
        self.inspection = "rpmdeps"
        self.result = "OK"
        self.waiver_auth = "Not Waivable"


class UnexpandedMacroRequiresCompareRPMs(TestCompareRPMs):
    def setUp(self):
        super().setUp()

        self.before_rpm.add_requires(unexpanded_requires)
        self.after_rpm.add_requires(unexpanded_requires)

        self.inspection = "rpmdeps"
        self.result = "BAD"
        self.waiver_auth = "Anyone"


class UnexpandedMacroRequiresCompareKoji(TestCompareKoji):
    def setUp(self):
        super().setUp()

        self.before_rpm.add_requires(unexpanded_requires)
        self.after_rpm.add_requires(unexpanded_requires)

        self.inspection = "rpmdeps"
        self.result = "BAD"
        self.waiver_auth = "Anyone"


# Missing explicit Requires (VERIFY)
class MissingExplicitRequiresSRPM(TestSRPM):
    def setUp(self):
        super().setUp()

        # add a subpackage
        self.rpm.add_subpackage("libs")

        # we need some stuff in the packages, first a shared library
        self.rpm.add_simple_library(
            libraryName="libvaporware.so",
            installPath="usr/lib/libvaporware.so",
            subpackageSuffix="libs",
        )

        # now add a program linked with that library
        sourceFileName = "main.c"
        installPath = "usr/bin/vaporware"
        self.rpm.add_source(SourceFile(sourceFileName, hello_world))
        self.rpm.section_build += (
            "%if 0%{?__isa_bits} == 32\n%define mopt -m32\n%endif\n"
        )
        self.rpm.section_build += (
            CC + " %%{?mopt} %s -L. -lvaporware\n" % sourceFileName
        )
        self.rpm.create_parent_dirs(installPath)
        self.rpm.section_install += "cp a.out $RPM_BUILD_ROOT/%s\n" % installPath
        binsub = self.rpm.get_subpackage(None)
        binsub.section_files += "/%s\n" % installPath
        self.rpm.add_payload_check(installPath, None)

        # result is OK because rpminspect can't report missing deps on SRPMs
        self.inspection = "rpmdeps"
        self.result = "OK"
        self.waiver_auth = "Not Waivable"


class MissingExplicitRequiresRPMs(TestRPMs):
    def setUp(self):
        super().setUp()

        # add a subpackage
        self.rpm.add_subpackage("libs")

        # we need some stuff in the packages, first a shared library
        self.rpm.add_simple_library(
            libraryName="libvaporware.so",
            installPath="usr/lib/libvaporware.so",
            subpackageSuffix="libs",
        )

        # now add a program linked with that library
        sourceFileName = "main.c"
        installPath = "usr/bin/vaporware"
        self.rpm.add_source(SourceFile(sourceFileName, hello_world))
        self.rpm.section_build += (
            "%if 0%{?__isa_bits} == 32\n%define mopt -m32\n%endif\n"
        )
        self.rpm.section_build += (
            CC + " %%{?mopt} %s -L. -lvaporware\n" % sourceFileName
        )
        self.rpm.create_parent_dirs(installPath)
        self.rpm.section_install += "cp a.out $RPM_BUILD_ROOT/%s\n" % installPath
        binsub = self.rpm.get_subpackage(None)
        binsub.section_files += "/%s\n" % installPath
        self.rpm.add_payload_check(installPath, None)

        # result is OK because rpminspect can't report missing deps when just
        # looking at a single RPM
        self.inspection = "rpmdeps"
        self.result = "OK"
        self.waiver_auth = "Not Waivable"


class MissingExplicitRequiresKoji(TestKoji):
    def setUp(self):
        super().setUp()

        # add a subpackage
        self.rpm.add_subpackage("libs")

        # we need some stuff in the packages, first a shared library
        self.rpm.add_simple_library(
            libraryName="libvaporware.so",
            installPath="usr/lib/libvaporware.so",
            subpackageSuffix="libs",
        )

        # now add a program linked with that library
        sourceFileName = "main.c"
        installPath = "usr/bin/vaporware"
        self.rpm.add_source(SourceFile(sourceFileName, hello_world))
        self.rpm.section_build += (
            "%if 0%{?__isa_bits} == 32\n%define mopt -m32\n%endif\n"
        )
        self.rpm.section_build += (
            CC + " %%{?mopt} %s -L. -lvaporware\n" % sourceFileName
        )
        self.rpm.create_parent_dirs(installPath)
        self.rpm.section_install += "cp a.out $RPM_BUILD_ROOT/%s\n" % installPath
        binsub = self.rpm.get_subpackage(None)
        binsub.section_files += "/%s\n" % installPath
        self.rpm.add_payload_check(installPath, None)

        self.inspection = "rpmdeps"
        self.result = "VERIFY"
        self.waiver_auth = "Anyone"


class MissingExplicitRequiresCompareSRPM(TestCompareSRPM):
    def setUp(self):
        super().setUp()

        # add a subpackage
        self.before_rpm.add_subpackage("libs")
        self.after_rpm.add_subpackage("libs")

        # we need some stuff in the packages, first a shared library
        self.before_rpm.add_simple_library(
            libraryName="libvaporware.so",
            installPath="usr/lib/libvaporware.so",
            subpackageSuffix="libs",
        )
        self.after_rpm.add_simple_library(
            libraryName="libvaporware.so",
            installPath="usr/lib/libvaporware.so",
            subpackageSuffix="libs",
        )

        # now add a program linked with that library
        sourceFileName = "main.c"
        installPath = "usr/bin/vaporware"

        self.before_rpm.add_source(SourceFile(sourceFileName, hello_world))
        self.before_rpm.section_build += (
            "%if 0%{?__isa_bits} == 32\n%define mopt -m32\n%endif\n"
        )
        self.before_rpm.section_build += (
            CC + " %%{?mopt} %s -L. -lvaporware\n" % sourceFileName
        )
        self.before_rpm.create_parent_dirs(installPath)
        self.before_rpm.section_install += "cp a.out $RPM_BUILD_ROOT/%s\n" % installPath
        binsub = self.before_rpm.get_subpackage(None)
        binsub.section_files += "/%s\n" % installPath
        self.before_rpm.add_payload_check(installPath, None)

        self.after_rpm.add_source(SourceFile(sourceFileName, hello_world))
        self.after_rpm.section_build += (
            "%if 0%{?__isa_bits} == 32\n%define mopt -m32\n%endif\n"
        )
        self.after_rpm.section_build += (
            CC + " %%{?mopt} %s -L. -lvaporware\n" % sourceFileName
        )
        self.after_rpm.create_parent_dirs(installPath)
        self.after_rpm.section_install += "cp a.out $RPM_BUILD_ROOT/%s\n" % installPath
        binsub = self.after_rpm.get_subpackage(None)
        binsub.section_files += "/%s\n" % installPath
        self.after_rpm.add_payload_check(installPath, None)

        # result is OK because rpminspect can't report missing deps on SRPMs
        self.inspection = "rpmdeps"
        self.result = "OK"
        self.waiver_auth = "Not Waivable"


class MissingExplicitRequiresCompareRPMs(TestCompareRPMs):
    def setUp(self):
        super().setUp()

        # add a subpackage
        self.before_rpm.add_subpackage("libs")
        self.after_rpm.add_subpackage("libs")

        # we need some stuff in the packages, first a shared library
        self.before_rpm.add_simple_library(
            libraryName="libvaporware.so",
            installPath="usr/lib/libvaporware.so",
            subpackageSuffix="libs",
        )
        self.after_rpm.add_simple_library(
            libraryName="libvaporware.so",
            installPath="usr/lib/libvaporware.so",
            subpackageSuffix="libs",
        )

        # now add a program linked with that library
        sourceFileName = "main.c"
        installPath = "usr/bin/vaporware"

        self.before_rpm.add_source(SourceFile(sourceFileName, hello_world))
        self.before_rpm.section_build += (
            "%if 0%{?__isa_bits} == 32\n%define mopt -m32\n%endif\n"
        )
        self.before_rpm.section_build += (
            CC + " %%{?mopt} %s -L. -lvaporware\n" % sourceFileName
        )
        self.before_rpm.create_parent_dirs(installPath)
        self.before_rpm.section_install += "cp a.out $RPM_BUILD_ROOT/%s\n" % installPath
        binsub = self.before_rpm.get_subpackage(None)
        binsub.section_files += "/%s\n" % installPath
        self.before_rpm.add_payload_check(installPath, None)

        self.after_rpm.add_source(SourceFile(sourceFileName, hello_world))
        self.after_rpm.section_build += (
            "%if 0%{?__isa_bits} == 32\n%define mopt -m32\n%endif\n"
        )
        self.after_rpm.section_build += (
            CC + " %%{?mopt} %s -L. -lvaporware\n" % sourceFileName
        )
        self.after_rpm.create_parent_dirs(installPath)
        self.after_rpm.section_install += "cp a.out $RPM_BUILD_ROOT/%s\n" % installPath
        binsub = self.after_rpm.get_subpackage(None)
        binsub.section_files += "/%s\n" % installPath
        self.after_rpm.add_payload_check(installPath, None)

        # result is OK because rpminspect can't report missing deps on single
        # RPM comparisons
        self.inspection = "rpmdeps"
        self.result = "OK"
        self.waiver_auth = "Not Waivable"


class MissingExplicitRequiresCompareKoji(TestCompareKoji):
    def setUp(self):
        super().setUp()

        # add a subpackage
        self.before_rpm.add_subpackage("libs")
        self.after_rpm.add_subpackage("libs")

        # we need some stuff in the packages, first a shared library
        self.before_rpm.add_simple_library(
            libraryName="libvaporware.so",
            installPath="usr/lib/libvaporware.so",
            subpackageSuffix="libs",
        )
        self.after_rpm.add_simple_library(
            libraryName="libvaporware.so",
            installPath="usr/lib/libvaporware.so",
            subpackageSuffix="libs",
        )

        # now add a program linked with that library
        sourceFileName = "main.c"
        installPath = "usr/bin/vaporware"

        self.before_rpm.add_source(SourceFile(sourceFileName, hello_world))
        self.before_rpm.section_build += (
            "%if 0%{?__isa_bits} == 32\n%define mopt -m32\n%endif\n"
        )
        self.before_rpm.section_build += (
            CC + " %%{?mopt} %s -L. -lvaporware\n" % sourceFileName
        )
        self.before_rpm.create_parent_dirs(installPath)
        self.before_rpm.section_install += "cp a.out $RPM_BUILD_ROOT/%s\n" % installPath
        binsub = self.before_rpm.get_subpackage(None)
        binsub.section_files += "/%s\n" % installPath
        self.before_rpm.add_payload_check(installPath, None)

        self.after_rpm.add_source(SourceFile(sourceFileName, hello_world))
        self.after_rpm.section_build += (
            "%if 0%{?__isa_bits} == 32\n%define mopt -m32\n%endif\n"
        )
        self.after_rpm.section_build += (
            CC + " %%{?mopt} %s -L. -lvaporware\n" % sourceFileName
        )
        self.after_rpm.create_parent_dirs(installPath)
        self.after_rpm.section_install += "cp a.out $RPM_BUILD_ROOT/%s\n" % installPath
        binsub = self.after_rpm.get_subpackage(None)
        binsub.section_files += "/%s\n" % installPath
        self.after_rpm.add_payload_check(installPath, None)

        self.inspection = "rpmdeps"
        self.result = "VERIFY"
        self.waiver_auth = "Anyone"