import Bio.PDB.Structure
from Bio.PDB import PDBIO, MMCIFIO
from Bio.PDB.mmtf.mmtfio import MMTFIO

from .modules.channels import x_channel, y_channel, z_channel
from .modules.input_file_parser import ParseInputFile
from .modules.atom_selection_config import SelectLayer

###################################################################
# Layers class that accepts the input file, out_dir and cut_off   #
# to calculate the surface.                                       #
#                                                                 #
# ------------------> Minimalistic Usage <------------------------#
#                                                                 #
# from MolLayers import engine                                    #
# data = engine.Layers('1a2y.pdb')                                  #
# data.calc_surface(peel_layers=True)                             #
##################################################################
class Layers():
    def __init__(self, file_name, out_dir='.', cut_off=1.52):
        #Adjusts the path variable before appending outfile to path
        if out_dir.endswith('/'):
            self.out_dir = out_dir
        else:
            self.out_dir = out_dir+'/'
        #cut off definition for channel is assigned
        self.cut_off = cut_off

        #File name including path is submitted to the Parser module
        self.molecule = ParseInputFile(file_name)
        #Keeps track of the atoms in a molecules if they are assigned
        # to surface or not
        self.molecule.processed_atoms = self.molecule.atoms
        #Variable that tracks the processing status, if layers calculation is
        # not complete then functions like RTP will check this variable before
        # enabling the layers algorithm
        self.calculated_layers = False
        self.layers_peeled = 0

    #Atom are labelled with layer number and if they are on surface or not
    def __label_atoms(self, channel, coordinate_axis, layer_number):
        channel.sort(key=lambda atom: atom.coord[coordinate_axis])
        if layer_number == 1:
            channel[0].is_surface = True
            channel[-1].is_surface = True
        channel[0].layer_number = layer_number
        channel[-1].layer_number = layer_number

    #Actual implementation of Layers algorithm, if peel_layers in set to TRUE
    # then all the layers will be peeled otherwise just the surface layer will
    # be peeled.
    def calc_surface(self, peel_layers=False,cut_off=None):
        if cut_off:
            self.cut_off=cut_off
            self.molecule.processed_atoms = self.molecule.atoms

        unfinished = True
        layer_number = 1

        if not peel_layers:
            print('Calculating surface for: ', self.molecule.structure_data)
        else:
            print('Calculating layers for: ', self.molecule.structure_data)

        self.layers_peeled = peel_layers
        while unfinished:
            if self.cut_off > 1.52:
                unfinished = False
                peel_layers = False
            print('Calculating layer: ', layer_number)
            for atom1 in self.molecule.processed_atoms:
                atom1.x_channel_atoms = []
                atom1.y_channel_atoms = []
                atom1.z_channel_atoms = []
                for atom2 in self.molecule.processed_atoms:
                    if x_channel(atom1, atom2) <= self.cut_off:
                        atom1.x_channel_atoms.append(atom2)
                    if y_channel(atom1, atom2) <= self.cut_off:
                        atom1.y_channel_atoms.append(atom2)
                    if z_channel(atom1, atom2) <= self.cut_off:
                        atom1.z_channel_atoms.append(atom2)

                if len(atom1.x_channel_atoms):
                    self.__label_atoms(atom1.x_channel_atoms, 0, layer_number)
                if len(atom1.y_channel_atoms):
                    self.__label_atoms(atom1.y_channel_atoms, 1, layer_number)
                if len(atom1.z_channel_atoms):
                    self.__label_atoms(atom1.z_channel_atoms, 2, layer_number)

            self.number_of_layers = layer_number

            if not 'layers' in self.molecule.__dict__.keys():
                self.molecule.__dict__['layers'] = {}
            #if requested to peel all layers then the atoms that are not
            # processed will be resubmitted to calculate layer and iterates
            # till all the atoms in the molecule are processed.
            if peel_layers:
                self.molecule.processed_atoms = []
                for atom in self.molecule.atoms:
                    if atom.disordered_flag == 0 and not atom.layer_number:
                        self.molecule.processed_atoms.append(atom)


                # If processed_atoms list is not empty, then
                # peel the layers for the unprocessed atoms.
                if self.molecule.processed_atoms:
                    unfinished = True
                else:
                    # if list is empty then all the atoms are processed
                    # then peeling can be terminated.
                    unfinished = False
                    print('Finished calculating layers')
                    #Since the entire molecule is peeled set calculated_layers = True
                    self.calculated_layers = True
                    #Write the surface with all the the layers.
                    self.write_surface(layers=True)
                    #Call the Residue Transition pattern to write the RTP into a outfile
                    self.calc_RTP()
                #Keeps track of the number of layers processed.
                layer_number += 1
            else:
                #If peel_layers is not enabled then surface of the molecule is calculated
                # or sampled based on the cut off value. Once calculation is done then
                # surface atoms will be written to an outfile.
                unfinished = False
                self.write_surface()

    #Internal function that selects the same output file format as input file format and
    #write the file in the same directory unless specified other using out_dir variable.
    def write_surface(self,layers=False):
        print('Started writing output')
        if self.molecule.input_file_extension in ['pdb', 'ent']:
            io = PDBIO()
        elif self.molecule.input_file_extension in ['cif']:
            io = MMCIFIO()
        elif self.molecule.input_file_extension in ['mmtf']:
            io = MMTFIO()

        io.set_structure(self.molecule.structure_data)

        if self.cut_off>1.52:
            out_name = self.out_dir + self.molecule.input_file_id + '_sampl_'+str(self.cut_off)+'.' + self.molecule.input_file_extension
        else:
            out_name = self.out_dir + self.molecule.input_file_id + '_surf1.' + self.molecule.input_file_extension

        if layers==True and self.calculated_layers==False:
            self.calc_surface(peel_layers=True)

        for layer in range(self.number_of_layers):
            layer += 1
            #out_name = self.out_dir + self.molecule.input_file_id + '_surf'+str(layer)+'.' + self.molecule.input_file_extension

            if self.molecule.input_file_extension in ['mmtf']:
                io.save(out_name, select=SelectLayer(layer))
            else:
                io.save(out_name, select=SelectLayer(layer), preserve_atom_numbering=True)
            if not layers:
                break
        print('Finished writing output to file: ', out_name)

    def calc_RTP(self):
        print('Started writing RTP')
        #Checks if all the layers were peeled or not, if not then the peeling of all layers is initiated.
        if not self.calculated_layers:
            print('Layers not peeled: Initiating layer algorithm')
            self.calc_surface(peel_layers=True)
            print('Layers algorithm implemented\nNow initiating RTP calculation')
        out_name = self.out_dir + self.molecule.input_file_id + '.RTP'
        out_file = open(out_name,'w')
        out_file.write('{0:s}{1:s}{2:s}{3:s}\n'.format('#RName', '#RNo.', '#Chain', '#RTP'))
        #RTP is assigned per residue, the layer number to a residue is assigned with the highest layer
        #number found among the atoms that belong to a residue.
        for model in self.molecule.structure_data:
            for chain in model:
                for residue in chain:
                    if residue.resname == 'HOH' or residue.disordered != 0:
                        continue
                    rtp=0
                    for atom in residue:
                        if rtp < atom.layer_number:
                            rtp = atom.layer_number
                    residue.rtp = rtp
                    #print('{0:<4s}{1:>6d}{2:>3s}{3:>3d}'.format(residue.resname,residue._id[1],chain._id,residue.rtp))
                    out_file.write('{0:<4s}{1:>6d}{2:>3s}{3:>3d}\n'.format(residue.resname, residue._id[1], chain._id, residue.rtp))
        print('RTP written into file: ', out_name)






