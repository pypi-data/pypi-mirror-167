import pytest
import unittest

from PyFoam.RunDictionary.ParsedBlockMeshDict import ParsedBlockMeshDict
from PyFoam.RunDictionary.SolutionDirectory import SolutionDirectory

from PyFoam.FoamInformation import oldTutorialStructure,foamTutorials,foamVersionNumber
from os import path, environ
from tempfile import mktemp
from shutil import rmtree, copy


def plateHoleTutorial():
    prefix=foamTutorials()
    if not oldTutorialStructure():
        prefix=path.join(prefix,"stressAnalysis")
    return path.join(prefix,"solidDisplacementFoam","plateHole")


@pytest.fixture(params=[pytest.param(None,
                                     marks=pytest.mark.skipif(foamTutorials()=='',reason="$FOAM_TUTORIALS is not defined")),
                        "v1812",
                        "v2112"])
def plate_hole_case(tmpdir, data_directory, empty_case, request):
    version = request.param
    dest = str(tmpdir)
    sol = SolutionDirectory(empty_case,
                            archive=None,
                            paraviewLink=False).cloneCase(dest)

    destMesh = sol.blockMesh()
    if destMesh == "":
        destMesh = path.join(sol.systemDir(), "blockMeshDict")

    if version is not None:
        copy(path.join(data_directory, "plateHole_blockmesh", version),
             destMesh)
    else:
        tut = SolutionDirectory(plateHoleTutorial(),
                                archive=None,
                                paraviewLink=False)
        copy(tut.blockMesh(), destMesh)

    yield dest

    rmtree(dest)


class ParsedBlockMeshDictTest:
    # def setUp(self):
    #     self.dest=mktemp()
    #     SolutionDirectory(plateHoleTutorial(),archive=None,paraviewLink=False).cloneCase(self.dest)

    # def tearDown(self):
    #     rmtree(self.dest)

    def testBoundaryRead(self, plate_hole_case):
        blk=ParsedBlockMeshDict(SolutionDirectory(plate_hole_case).blockMesh())
        assert blk.convertToMeters() == 1.
        assert len(blk.vertices()) == 22
        assert len(blk.blocks()) == 5
        assert len(blk.patches()) == 6
        assert len(blk.arcs()) == 8
        assert blk.typicalLength() == 1.25
        assert str(blk.getBounds()) == "([0.0, 0.0, 0.0], [2.0, 2.0, 0.5])"

    def testRoundtripBlockMesh(self, plate_hole_case):
        blk=ParsedBlockMeshDict(SolutionDirectory(plate_hole_case).blockMesh())
        txt=str(blk)
        try:
            i=int(txt.split("blocks")[1].split("(")[0])
            assert False
        except ValueError:
            pass
