from typing import Any, List

from typing import overload
import Kratos
AMOUNT_OF_COHESION_FROM_STRESS: Kratos.DoubleVariable
ANGULAR_VELOCITY_START_TIME: Kratos.DoubleVariable
ANGULAR_VELOCITY_STOP_TIME: Kratos.DoubleVariable
AREA_VERTICAL_CENTRE: Kratos.DoubleVariable
AREA_VERTICAL_TAPA: Kratos.DoubleVariable
AUTOMATIC_SKIN_COMPUTATION: Kratos.BoolVariable
AUX_ORIENTATION: Kratos.DoubleQuaternionVariable
BEAM_INERTIA_ROT_UNIT_LENGHT_X: Kratos.DoubleVariable
BEAM_INERTIA_ROT_UNIT_LENGHT_Y: Kratos.DoubleVariable
BEAM_INERTIA_ROT_UNIT_LENGHT_Z: Kratos.DoubleVariable
BEAM_LENGTH: Kratos.DoubleVariable
BEAM_PARTICLES_DISTANCE: Kratos.DoubleVariable
BLAST_BOREHOLE: Kratos.IntegerVariable
BLAST_COORDINATES_1: Kratos.Array1DVariable3
BLAST_COORDINATES_1_X: Kratos.DoubleVariable
BLAST_COORDINATES_1_Y: Kratos.DoubleVariable
BLAST_COORDINATES_1_Z: Kratos.DoubleVariable
BLAST_COORDINATES_2: Kratos.Array1DVariable3
BLAST_COORDINATES_2_X: Kratos.DoubleVariable
BLAST_COORDINATES_2_Y: Kratos.DoubleVariable
BLAST_COORDINATES_2_Z: Kratos.DoubleVariable
BLAST_COORDINATES_3: Kratos.Array1DVariable3
BLAST_COORDINATES_3_X: Kratos.DoubleVariable
BLAST_COORDINATES_3_Y: Kratos.DoubleVariable
BLAST_COORDINATES_3_Z: Kratos.DoubleVariable
BLAST_COORDINATES_4: Kratos.Array1DVariable3
BLAST_COORDINATES_4_X: Kratos.DoubleVariable
BLAST_COORDINATES_4_Y: Kratos.DoubleVariable
BLAST_COORDINATES_4_Z: Kratos.DoubleVariable
BLAST_COORDINATES_5: Kratos.Array1DVariable3
BLAST_COORDINATES_5_X: Kratos.DoubleVariable
BLAST_COORDINATES_5_Y: Kratos.DoubleVariable
BLAST_COORDINATES_5_Z: Kratos.DoubleVariable
BLAST_COORDINATES_6: Kratos.Array1DVariable3
BLAST_COORDINATES_6_X: Kratos.DoubleVariable
BLAST_COORDINATES_6_Y: Kratos.DoubleVariable
BLAST_COORDINATES_6_Z: Kratos.DoubleVariable
BLAST_COORDINATES_7: Kratos.Array1DVariable3
BLAST_COORDINATES_7_X: Kratos.DoubleVariable
BLAST_COORDINATES_7_Y: Kratos.DoubleVariable
BLAST_COORDINATES_7_Z: Kratos.DoubleVariable
BLAST_COORDINATES_8: Kratos.Array1DVariable3
BLAST_COORDINATES_8_X: Kratos.DoubleVariable
BLAST_COORDINATES_8_Y: Kratos.DoubleVariable
BLAST_COORDINATES_8_Z: Kratos.DoubleVariable
BLAST_CURVE: Kratos.IntegerVariable
BLAST_NPOINTS: Kratos.IntegerVariable
BLAST_PRESSURE_MAX: Kratos.DoubleVariable
BLAST_RADIUS: Kratos.DoubleVariable
BLAST_SHAPE_FACTOR: Kratos.DoubleVariable
BLAST_TIME_DELAY: Kratos.DoubleVariable
BLAST_TIME_PRESSURE_MAX: Kratos.DoubleVariable
BONDED_MATERIAL_YOUNG_MODULUS: Kratos.DoubleVariable
BOTTOM: Kratos.IntegerVariable
BOUNDING_BOX_OPTION: Kratos.IntegerVariable
BOUNDING_BOX_START_TIME: Kratos.DoubleVariable
BOUNDING_BOX_STOP_TIME: Kratos.DoubleVariable
BREAKABLE_CLUSTER: Kratos.BoolVariable
BRINELL_HARDNESS: Kratos.DoubleVariable
CASE_OPTION: Kratos.IntegerVariable
CHARACTERISTIC_LENGTH: Kratos.DoubleVariable
CLEAN_INDENT_OPTION: Kratos.IntegerVariable
CLUSTER_FILE_NAME: Kratos.StringVariable
CLUSTER_VOLUME: Kratos.DoubleVariable
COEFFICIENT_OF_RESTITUTION: Kratos.DoubleVariable
COHESIVE_GROUP: Kratos.IntegerVariable
COMPUTE_ENERGY_OPTION: Kratos.IntegerVariable
COMPUTE_FEM_RESULTS_OPTION: Kratos.IntegerVariable
COMPUTE_STRESS_TENSOR_OPTION: Kratos.IntegerVariable
COMPUTE_WEAR: Kratos.BoolVariable
CONCRETE_TEST_OPTION: Kratos.IntegerVariable
CONICAL_DAMAGE_ALPHA: Kratos.DoubleVariable
CONICAL_DAMAGE_ALPHA_FUNCTION: Kratos.DoubleVariable
CONICAL_DAMAGE_CONTACT_RADIUS: Kratos.DoubleVariable
CONICAL_DAMAGE_GAMMA: Kratos.DoubleVariable
CONICAL_DAMAGE_MAX_STRESS: Kratos.DoubleVariable
CONTACT_FAILURE: Kratos.DoubleVariable
CONTACT_FORCES: Kratos.Array1DVariable3
CONTACT_FORCES_X: Kratos.DoubleVariable
CONTACT_FORCES_Y: Kratos.DoubleVariable
CONTACT_FORCES_Z: Kratos.DoubleVariable
CONTACT_IMPULSE: Kratos.Array1DVariable3
CONTACT_IMPULSE_X: Kratos.DoubleVariable
CONTACT_IMPULSE_Y: Kratos.DoubleVariable
CONTACT_IMPULSE_Z: Kratos.DoubleVariable
CONTACT_INTERNAL_FRICC: Kratos.DoubleVariable
CONTACT_MESH_OPTION: Kratos.IntegerVariable
CONTACT_ORIENTATION: Kratos.DoubleVariable
CONTACT_SIGMA: Kratos.DoubleVariable
CONTACT_SIGMA_MIN: Kratos.DoubleVariable
CONTACT_TAU: Kratos.DoubleVariable
CONTACT_TAU_ZERO: Kratos.DoubleVariable
CONTAINS_CLUSTERS: Kratos.BoolVariable
CONTINUUM_OPTION: Kratos.IntegerVariable
CONTINUUM_SEARCH_RADIUS_AMPLIFICATION_FACTOR: Kratos.DoubleVariable
COORDINATION_NUMBER: Kratos.DoubleVariable
CROSS_AREA: Kratos.DoubleVariable
DAMAGE_FACTOR: Kratos.DoubleVariable
DAMPING_GAMMA: Kratos.DoubleVariable
DEBUG_PRINTING_ID_1: Kratos.IntegerVariable
DEBUG_PRINTING_ID_2: Kratos.IntegerVariable
DEBUG_PRINTING_OPTION: Kratos.BoolVariable
DELTA_DISPLACEMENT: Kratos.Array1DVariable3
DELTA_DISPLACEMENT_X: Kratos.DoubleVariable
DELTA_DISPLACEMENT_Y: Kratos.DoubleVariable
DELTA_DISPLACEMENT_Z: Kratos.DoubleVariable
DELTA_OPTION: Kratos.BoolVariable
DELTA_ROTA_DISPLACEMENT: Kratos.Array1DVariable3
DELTA_ROTA_DISPLACEMENT_X: Kratos.DoubleVariable
DELTA_ROTA_DISPLACEMENT_Y: Kratos.DoubleVariable
DELTA_ROTA_DISPLACEMENT_Z: Kratos.DoubleVariable
DEM_BEAM_CONSTITUTIVE_LAW_POINTER: DEMBeamConstitutiveLawPointerVariable
DEM_CONTINUUM_CONSTITUTIVE_LAW_NAME: Kratos.StringVariable
DEM_CONTINUUM_CONSTITUTIVE_LAW_POINTER: DEMContinuumConstitutiveLawPointerVariable
DEM_DIFFERENTIAL_STRAIN_TENSOR: Kratos.MatrixVariable
DEM_DISCONTINUUM_CONSTITUTIVE_LAW_NAME: Kratos.StringVariable
DEM_DISCONTINUUM_CONSTITUTIVE_LAW_POINTER: DEMDiscontinuumConstitutiveLawPointerVariable
DEM_DRAG_CONSTANT_X: Kratos.DoubleVariable
DEM_DRAG_CONSTANT_Y: Kratos.DoubleVariable
DEM_DRAG_CONSTANT_Z: Kratos.DoubleVariable
DEM_ENGINE_PERFORMANCE: Kratos.DoubleVariable
DEM_ENGINE_POWER: Kratos.DoubleVariable
DEM_MAX_ENGINE_FORCE: Kratos.DoubleVariable
DEM_M_CAMCLAY_SLOPE: Kratos.DoubleVariable
DEM_NODAL_AREA: Kratos.DoubleVariable
DEM_PRECONSOLIDATION_PRESSURE: Kratos.DoubleVariable
DEM_PRESSURE: Kratos.DoubleVariable
DEM_ROTATIONAL_INTEGRATION_SCHEME_NAME: Kratos.StringVariable
DEM_ROTATIONAL_INTEGRATION_SCHEME_POINTER: DEMIntegrationSchemePointerVariable
DEM_STRAIN_TENSOR: Kratos.MatrixVariable
DEM_STRESS_TENSOR: Kratos.MatrixVariable
DEM_THRESHOLD_VELOCITY: Kratos.DoubleVariable
DEM_TRANSLATIONAL_INTEGRATION_SCHEME_NAME: Kratos.StringVariable
DEM_TRANSLATIONAL_INTEGRATION_SCHEME_POINTER: DEMIntegrationSchemePointerVariable
DENSE_INLET: Kratos.BoolVariable
DEVIATION: Kratos.DoubleVariable
DOMAIN_IS_PERIODIC: Kratos.BoolVariable
DOMAIN_MAX_CORNER: Kratos.Array1DVariable3
DOMAIN_MAX_CORNER_X: Kratos.DoubleVariable
DOMAIN_MAX_CORNER_Y: Kratos.DoubleVariable
DOMAIN_MAX_CORNER_Z: Kratos.DoubleVariable
DOMAIN_MIN_CORNER: Kratos.Array1DVariable3
DOMAIN_MIN_CORNER_X: Kratos.DoubleVariable
DOMAIN_MIN_CORNER_Y: Kratos.DoubleVariable
DOMAIN_MIN_CORNER_Z: Kratos.DoubleVariable
DONZE_G1: Kratos.DoubleVariable
DONZE_G2: Kratos.DoubleVariable
DONZE_G3: Kratos.DoubleVariable
DONZE_MAX_DEF: Kratos.DoubleVariable
DUMMY_SWITCH: Kratos.IntegerVariable
DYNAMIC_FRICTION: Kratos.DoubleVariable
ELASTIC_FORCES: Kratos.Array1DVariable3
ELASTIC_FORCES_X: Kratos.DoubleVariable
ELASTIC_FORCES_Y: Kratos.DoubleVariable
ELASTIC_FORCES_Z: Kratos.DoubleVariable
ELASTIC_REACTION_STRESS: Kratos.Array1DVariable3
ELASTIC_REACTION_STRESS_X: Kratos.DoubleVariable
ELASTIC_REACTION_STRESS_Y: Kratos.DoubleVariable
ELASTIC_REACTION_STRESS_Z: Kratos.DoubleVariable
EULER_ANGLES: Kratos.Array1DVariable3
EULER_ANGLES_X: Kratos.DoubleVariable
EULER_ANGLES_Y: Kratos.DoubleVariable
EULER_ANGLES_Z: Kratos.DoubleVariable
EXCENTRICITY: Kratos.DoubleVariable
EXCENTRICITY_PROBABILITY_DISTRIBUTION: Kratos.StringVariable
EXCENTRICITY_STANDARD_DEVIATION: Kratos.DoubleVariable
EXPORT_ID: Kratos.DoubleVariable
EXPORT_PARTICLE_FAILURE_ID: Kratos.DoubleVariable
FACE_NORMAL_IMPACT_VELOCITY: Kratos.DoubleVariable
FACE_TANGENTIAL_IMPACT_VELOCITY: Kratos.DoubleVariable
FAILURE_CRITERION_STATE: Kratos.DoubleVariable
FIXED_VEL_BOT: Kratos.DoubleVariable
FIXED_VEL_TOP: Kratos.DoubleVariable
FIX_VELOCITIES_FLAG: Kratos.IntegerVariable
FLOATING_OPTION: Kratos.IntegerVariable
FORCE_INTEGRATION_GROUP: Kratos.IntegerVariable
FORCE_REACTION: Kratos.Array1DVariable3
FORCE_REACTION_X: Kratos.DoubleVariable
FORCE_REACTION_Y: Kratos.DoubleVariable
FORCE_REACTION_Z: Kratos.DoubleVariable
FRACTURE_ENERGY: Kratos.DoubleVariable
FREE_BODY_MOTION: Kratos.IntegerVariable
FRICTION: Kratos.DoubleVariable
FRICTION_DECAY: Kratos.DoubleVariable
GLOBAL_COORDINATION_NUMBER_OPTION: Kratos.BoolVariable
GLOBAL_DAMPING: Kratos.DoubleVariable
HISTORICAL_MIN_K: Kratos.DoubleVariable
I22: Kratos.DoubleVariable
I33: Kratos.DoubleVariable
IF_BOUNDARY_ELEMENT: Kratos.IntegerVariable
IMPACT_WEAR: Kratos.DoubleVariable
IMPACT_WEAR_SEVERITY: Kratos.DoubleVariable
IMPOSED_MASS_FLOW_OPTION: Kratos.BoolVariable
IMPOSED_Z_STRAIN_OPTION: Kratos.BoolVariable
IMPOSED_Z_STRAIN_VALUE: Kratos.DoubleVariable
INITIAL_ANGULAR_VELOCITY_X_VALUE: Kratos.DoubleVariable
INITIAL_ANGULAR_VELOCITY_Y_VALUE: Kratos.DoubleVariable
INITIAL_ANGULAR_VELOCITY_Z_VALUE: Kratos.DoubleVariable
INITIAL_COHESION: Kratos.DoubleVariable
INITIAL_RADIUS: Kratos.DoubleVariable
INITIAL_ROTA_MOMENT: Kratos.Array1DVariable3
INITIAL_ROTA_MOMENT_X: Kratos.DoubleVariable
INITIAL_ROTA_MOMENT_Y: Kratos.DoubleVariable
INITIAL_ROTA_MOMENT_Z: Kratos.DoubleVariable
INITIAL_VELOCITY_X_VALUE: Kratos.DoubleVariable
INITIAL_VELOCITY_Y_VALUE: Kratos.DoubleVariable
INITIAL_VELOCITY_Z_VALUE: Kratos.DoubleVariable
INJECTOR_ELEMENT_TYPE: Kratos.StringVariable
INLET_INITIAL_PARTICLES_VELOCITY: Kratos.Array1DVariable3
INLET_INITIAL_PARTICLES_VELOCITY_X: Kratos.DoubleVariable
INLET_INITIAL_PARTICLES_VELOCITY_Y: Kratos.DoubleVariable
INLET_INITIAL_PARTICLES_VELOCITY_Z: Kratos.DoubleVariable
INLET_INITIAL_VELOCITY: Kratos.Array1DVariable3
INLET_INITIAL_VELOCITY_X: Kratos.DoubleVariable
INLET_INITIAL_VELOCITY_Y: Kratos.DoubleVariable
INLET_INITIAL_VELOCITY_Z: Kratos.DoubleVariable
INLET_MAX_PARTICLES_VELOCITY: Kratos.DoubleVariable
INLET_NUMBER_OF_PARTICLES: Kratos.DoubleVariable
INLET_START_TIME: Kratos.DoubleVariable
INLET_STOP_TIME: Kratos.DoubleVariable
INTERNAL_COHESION: Kratos.DoubleVariable
INTERNAL_FRICTION_AFTER_THRESHOLD: Kratos.DoubleVariable
IS_GHOST: Kratos.BoolVariable
IS_STICKY: Kratos.BoolVariable
IS_TIME_TO_PRINT: Kratos.BoolVariable
KDEM_STANDARD_DEVIATION_FRICTION: Kratos.DoubleVariable
KDEM_STANDARD_DEVIATION_TAU_ZERO: Kratos.DoubleVariable
K_NORMAL: Kratos.DoubleVariable
K_TANGENTIAL: Kratos.DoubleVariable
LEVEL_OF_FOULING: Kratos.DoubleVariable
LINEAR_IMPULSE: Kratos.DoubleVariable
LINEAR_VELOCITY: Kratos.Array1DVariable3
LINEAR_VELOCITY_X: Kratos.DoubleVariable
LINEAR_VELOCITY_Y: Kratos.DoubleVariable
LINEAR_VELOCITY_Z: Kratos.DoubleVariable
LOADING_VELOCITY: Kratos.Array1DVariable3
LOADING_VELOCITY_X: Kratos.DoubleVariable
LOADING_VELOCITY_Y: Kratos.DoubleVariable
LOADING_VELOCITY_Z: Kratos.DoubleVariable
LOCAL_ANGULAR_VELOCITY: Kratos.Array1DVariable3
LOCAL_ANGULAR_VELOCITY_X: Kratos.DoubleVariable
LOCAL_ANGULAR_VELOCITY_Y: Kratos.DoubleVariable
LOCAL_ANGULAR_VELOCITY_Z: Kratos.DoubleVariable
LOCAL_AUX_ANGULAR_VELOCITY: Kratos.Array1DVariable3
LOCAL_AUX_ANGULAR_VELOCITY_X: Kratos.DoubleVariable
LOCAL_AUX_ANGULAR_VELOCITY_Y: Kratos.DoubleVariable
LOCAL_AUX_ANGULAR_VELOCITY_Z: Kratos.DoubleVariable
LOCAL_CONTACT_AREA_HIGH: Kratos.DoubleVariable
LOCAL_CONTACT_AREA_LOW: Kratos.DoubleVariable
LOCAL_CONTACT_FORCE: Kratos.Array1DVariable3
LOCAL_CONTACT_FORCE_X: Kratos.DoubleVariable
LOCAL_CONTACT_FORCE_Y: Kratos.DoubleVariable
LOCAL_CONTACT_FORCE_Z: Kratos.DoubleVariable
LOCAL_COORDINATION_NUMBER_OPTION: Kratos.BoolVariable
LOCAL_DAMP_RATIO: Kratos.DoubleVariable
LOCAL_RESOLUTION_METHOD: Kratos.IntegerVariable
LOOSE_MATERIAL_YOUNG_MODULUS: Kratos.DoubleVariable
MASS_FLOW: Kratos.DoubleVariable
MAXIMUM_RADIUS: Kratos.DoubleVariable
MAX_AMPLIFICATION_RATIO_OF_THE_SEARCH_RADIUS: Kratos.DoubleVariable
MAX_NUMBER_OF_INTACT_BONDS_TO_CONSIDER_A_SPHERE_BROKEN: Kratos.DoubleVariable
MAX_RAND_DEVIATION_ANGLE: Kratos.DoubleVariable
MAX_ROTA_MOMENT: Kratos.Array1DVariable3
MAX_ROTA_MOMENT_X: Kratos.DoubleVariable
MAX_ROTA_MOMENT_Y: Kratos.DoubleVariable
MAX_ROTA_MOMENT_Z: Kratos.DoubleVariable
MEAN_CONTACT_AREA: Kratos.DoubleVariable
MINIMUM_RADIUS: Kratos.DoubleVariable
MOMENT_REACTION: Kratos.Array1DVariable3
MOMENT_REACTION_X: Kratos.DoubleVariable
MOMENT_REACTION_Y: Kratos.DoubleVariable
MOMENT_REACTION_Z: Kratos.DoubleVariable
NEIGHBOUR_RATIO: Kratos.DoubleVariable
NEIGHBOUR_SIZE: Kratos.DoubleVariable
NEIGH_INITIALIZED: Kratos.IntegerVariable
NODAL_MASS_COEFF: Kratos.DoubleVariable
NON_DIMENSIONAL_VOLUME_WEAR: Kratos.DoubleVariable
NORMAL_IMPACT_VELOCITY: Kratos.DoubleVariable
PARTICLE_COHESION: Kratos.DoubleVariable
PARTICLE_DENSITY: Kratos.DoubleVariable
PARTICLE_ELASTIC_ENERGY: Kratos.DoubleVariable
PARTICLE_GRAVITATIONAL_ENERGY: Kratos.DoubleVariable
PARTICLE_ID: Kratos.IntegerVariable
PARTICLE_INELASTIC_FRICTIONAL_ENERGY: Kratos.DoubleVariable
PARTICLE_INELASTIC_VISCODAMPING_ENERGY: Kratos.DoubleVariable
PARTICLE_INERTIA: Kratos.DoubleVariable
PARTICLE_MOMENT: Kratos.Array1DVariable3
PARTICLE_MOMENT_OF_INERTIA: Kratos.DoubleVariable
PARTICLE_MOMENT_X: Kratos.DoubleVariable
PARTICLE_MOMENT_Y: Kratos.DoubleVariable
PARTICLE_MOMENT_Z: Kratos.DoubleVariable
PARTICLE_ROTATIONAL_KINEMATIC_ENERGY: Kratos.DoubleVariable
PARTICLE_ROTATION_ANGLE: Kratos.Array1DVariable3
PARTICLE_ROTATION_ANGLE_X: Kratos.DoubleVariable
PARTICLE_ROTATION_ANGLE_Y: Kratos.DoubleVariable
PARTICLE_ROTATION_ANGLE_Z: Kratos.DoubleVariable
PARTICLE_ROTATION_DAMP_RATIO: Kratos.DoubleVariable
PARTICLE_TENSION: Kratos.DoubleVariable
PARTICLE_TRANSLATIONAL_KINEMATIC_ENERGY: Kratos.DoubleVariable
PERTURBED_INTERNAL_FRICTION: Kratos.DoubleVariable
PERTURBED_TAU_ZERO: Kratos.DoubleVariable
PLASTIC_YIELD_STRESS: Kratos.DoubleVariable
POISSON_EFFECT_OPTION: Kratos.IntegerVariable
POISSON_VALUE: Kratos.DoubleVariable
PRINCIPAL_MOMENTS_OF_INERTIA: Kratos.Array1DVariable3
PRINCIPAL_MOMENTS_OF_INERTIA_X: Kratos.DoubleVariable
PRINCIPAL_MOMENTS_OF_INERTIA_Y: Kratos.DoubleVariable
PRINCIPAL_MOMENTS_OF_INERTIA_Z: Kratos.DoubleVariable
PRINT_EXPORT_ID: Kratos.IntegerVariable
PRINT_STRESS_TENSOR_OPTION: Kratos.IntegerVariable
PROBABILITY_DISTRIBUTION: Kratos.StringVariable
PROPERTIES_ID: Kratos.IntegerVariable
RANDOM_ORIENTATION: Kratos.BoolVariable
REACTION_STRESS: Kratos.Array1DVariable3
REACTION_STRESS_X: Kratos.DoubleVariable
REACTION_STRESS_Y: Kratos.DoubleVariable
REACTION_STRESS_Z: Kratos.DoubleVariable
REPRESENTATIVE_VOLUME: Kratos.DoubleVariable
RIGID_BODY_CENTER_OF_MASS: Kratos.Array1DVariable3
RIGID_BODY_CENTER_OF_MASS_X: Kratos.DoubleVariable
RIGID_BODY_CENTER_OF_MASS_Y: Kratos.DoubleVariable
RIGID_BODY_CENTER_OF_MASS_Z: Kratos.DoubleVariable
RIGID_BODY_INERTIAS: Kratos.Array1DVariable3
RIGID_BODY_INERTIAS_X: Kratos.DoubleVariable
RIGID_BODY_INERTIAS_Y: Kratos.DoubleVariable
RIGID_BODY_INERTIAS_Z: Kratos.DoubleVariable
RIGID_BODY_MASS: Kratos.DoubleVariable
RIGID_BODY_MOTION: Kratos.IntegerVariable
RIGID_BODY_OPTION: Kratos.BoolVariable
RIGID_ELEMENT_FORCE: Kratos.Array1DVariable3
RIGID_ELEMENT_FORCE_X: Kratos.DoubleVariable
RIGID_ELEMENT_FORCE_Y: Kratos.DoubleVariable
RIGID_ELEMENT_FORCE_Z: Kratos.DoubleVariable
RIGID_FACE_AXIAL_SPEED: Kratos.DoubleVariable
RIGID_FACE_BEGIN_TIME: Kratos.DoubleVariable
RIGID_FACE_END_TIME: Kratos.DoubleVariable
RIGID_FACE_FLAG: Kratos.IntegerVariable
RIGID_FACE_PROP_ID: Kratos.IntegerVariable
RIGID_FACE_ROTA_AXIAL_DIR: Kratos.Array1DVariable3
RIGID_FACE_ROTA_AXIAL_DIR_X: Kratos.DoubleVariable
RIGID_FACE_ROTA_AXIAL_DIR_Y: Kratos.DoubleVariable
RIGID_FACE_ROTA_AXIAL_DIR_Z: Kratos.DoubleVariable
RIGID_FACE_ROTA_GLOBAL_VELOCITY: Kratos.Array1DVariable3
RIGID_FACE_ROTA_GLOBAL_VELOCITY_X: Kratos.DoubleVariable
RIGID_FACE_ROTA_GLOBAL_VELOCITY_Y: Kratos.DoubleVariable
RIGID_FACE_ROTA_GLOBAL_VELOCITY_Z: Kratos.DoubleVariable
RIGID_FACE_ROTA_ORIGIN_COORD: Kratos.Array1DVariable3
RIGID_FACE_ROTA_ORIGIN_COORD_X: Kratos.DoubleVariable
RIGID_FACE_ROTA_ORIGIN_COORD_Y: Kratos.DoubleVariable
RIGID_FACE_ROTA_ORIGIN_COORD_Z: Kratos.DoubleVariable
RIGID_FACE_ROTA_SPEED: Kratos.DoubleVariable
ROLLING_FRICTION: Kratos.DoubleVariable
ROLLING_FRICTION_OPTION: Kratos.IntegerVariable
ROLLING_FRICTION_WITH_WALLS: Kratos.DoubleVariable
ROLLING_RESISTANCE_MOMENT: Kratos.Array1DVariable3
ROLLING_RESISTANCE_MOMENT_X: Kratos.DoubleVariable
ROLLING_RESISTANCE_MOMENT_Y: Kratos.DoubleVariable
ROLLING_RESISTANCE_MOMENT_Z: Kratos.DoubleVariable
ROTATIONAL_MOMENT_COEFFICIENT: Kratos.DoubleVariable
ROTATION_OPTION: Kratos.IntegerVariable
SEARCH_CONTROL: Kratos.IntegerVariable
SEARCH_RADIUS_INCREMENT_FOR_BONDS_CREATION: Kratos.DoubleVariable
SEVERITY_OF_WEAR: Kratos.DoubleVariable
SHEAR_ENERGY_COEF: Kratos.DoubleVariable
SHEAR_STRAIN_PARALLEL_TO_BOND_OPTION: Kratos.IntegerVariable
SHEAR_STRESS: Kratos.DoubleVariable
SIGMA_3_AVERAGE: Kratos.DoubleVariable
SIGMA_SLOPE_CHANGE_THRESHOLD: Kratos.DoubleVariable
SKIN_FACTOR_RADIUS: Kratos.DoubleVariable
SKIN_SPHERE: Kratos.DoubleVariable
SLOPE_FRACTION_N1: Kratos.DoubleVariable
SLOPE_FRACTION_N2: Kratos.DoubleVariable
SLOPE_FRACTION_N3: Kratos.DoubleVariable
SLOPE_LIMIT_COEFF_C1: Kratos.DoubleVariable
SLOPE_LIMIT_COEFF_C2: Kratos.DoubleVariable
SLOPE_LIMIT_COEFF_C3: Kratos.DoubleVariable
SMOOTHED_ELASTIC_REACTION_STRESS: Kratos.Array1DVariable3
SMOOTHED_ELASTIC_REACTION_STRESS_X: Kratos.DoubleVariable
SMOOTHED_ELASTIC_REACTION_STRESS_Y: Kratos.DoubleVariable
SMOOTHED_ELASTIC_REACTION_STRESS_Z: Kratos.DoubleVariable
SMOOTHED_REACTION_STRESS: Kratos.Array1DVariable3
SMOOTHED_REACTION_STRESS_X: Kratos.DoubleVariable
SMOOTHED_REACTION_STRESS_Y: Kratos.DoubleVariable
SMOOTHED_REACTION_STRESS_Z: Kratos.DoubleVariable
SPRAYED_MATERIAL: Kratos.DoubleVariable
STANDARD_DEVIATION: Kratos.DoubleVariable
STATIC_FRICTION: Kratos.DoubleVariable
TABLE_NUMBER_ANGULAR_VELOCITY: Kratos.Array1DVariable3
TABLE_NUMBER_ANGULAR_VELOCITY_X: Kratos.DoubleVariable
TABLE_NUMBER_ANGULAR_VELOCITY_Y: Kratos.DoubleVariable
TABLE_NUMBER_ANGULAR_VELOCITY_Z: Kratos.DoubleVariable
TABLE_NUMBER_FORCE: Kratos.Array1DVariable3
TABLE_NUMBER_FORCE_X: Kratos.DoubleVariable
TABLE_NUMBER_FORCE_Y: Kratos.DoubleVariable
TABLE_NUMBER_FORCE_Z: Kratos.DoubleVariable
TABLE_NUMBER_MOMENT: Kratos.Array1DVariable3
TABLE_NUMBER_MOMENT_X: Kratos.DoubleVariable
TABLE_NUMBER_MOMENT_Y: Kratos.DoubleVariable
TABLE_NUMBER_MOMENT_Z: Kratos.DoubleVariable
TABLE_NUMBER_VELOCITY: Kratos.Array1DVariable3
TABLE_NUMBER_VELOCITY_X: Kratos.DoubleVariable
TABLE_NUMBER_VELOCITY_Y: Kratos.DoubleVariable
TABLE_NUMBER_VELOCITY_Z: Kratos.DoubleVariable
TANGENTIAL_ELASTIC_FORCES: Kratos.Array1DVariable3
TANGENTIAL_ELASTIC_FORCES_X: Kratos.DoubleVariable
TANGENTIAL_ELASTIC_FORCES_Y: Kratos.DoubleVariable
TANGENTIAL_ELASTIC_FORCES_Z: Kratos.DoubleVariable
TANGENTIAL_IMPACT_VELOCITY: Kratos.DoubleVariable
TARGET_STRESS: Kratos.Array1DVariable3
TARGET_STRESS_X: Kratos.DoubleVariable
TARGET_STRESS_Y: Kratos.DoubleVariable
TARGET_STRESS_Z: Kratos.DoubleVariable
TENSION_LIMIT_INCREASE_SLOPE: Kratos.DoubleVariable
TOP: Kratos.IntegerVariable
TRIAXIAL_TEST_OPTION: Kratos.IntegerVariable
TRIHEDRON_OPTION: Kratos.IntegerVariable
UNIDIMENSIONAL_DAMAGE: Kratos.DoubleVariable
VELOCITY_START_TIME: Kratos.DoubleVariable
VELOCITY_STOP_TIME: Kratos.DoubleVariable
VIRTUAL_MASS_OPTION: Kratos.IntegerVariable
WALL_COHESION: Kratos.DoubleVariable
YOUNG_MODULUS_PLASTIC: Kratos.DoubleVariable

class AnalyticFaceWatcher:
    def __init__(self, arg0: Kratos.ModelPart) -> None: ...
    def ClearData(self) -> None: ...
    def GetTotalFlux(self, arg0: list, arg1: list, arg2: list, arg3: list, arg4: list) -> None: ...
    def MakeMeasurements(self) -> None: ...

class AnalyticModelPartFiller:
    def __init__(self) -> None: ...
    def FillAnalyticModelPartGivenFractionOfParticlesToTransform(self, fraction_of_particles_to_convert: float, spheres_model_part: Kratos.ModelPart, particle_creator_destructor: ParticleCreatorDestructor, analytic_sub_model_part_name: str = ...) -> None: ...

class AnalyticParticleWatcher:
    def __init__(self) -> None: ...
    def MakeMeasurements(self, arg0: Kratos.ModelPart) -> None: ...
    def SetNodalMaxFaceImpactVelocities(self, arg0: Kratos.ModelPart) -> None: ...
    def SetNodalMaxImpactVelocities(self, arg0: Kratos.ModelPart) -> None: ...

class AnalyticWatcher:
    def __init__(self) -> None: ...

class ApplyForcesAndMomentsProcess(Kratos.Process):
    def __init__(self, arg0: Kratos.ModelPart, arg1: Kratos.Parameters) -> None: ...

class ApplyKinematicConstraintsProcess(Kratos.Process):
    def __init__(self, arg0: Kratos.ModelPart, arg1: Kratos.Parameters) -> None: ...

class AutomaticDTProcess(Kratos.Process):
    def __init__(self, arg0: Kratos.ModelPart, arg1: Kratos.Parameters) -> None: ...

class AuxiliaryUtilities:
    def __init__(self) -> None: ...
    def ComputeAverageZStressFor2D(self, arg0: Kratos.ModelPart) -> float: ...
    def UpdateTimeInOneModelPart(self, arg0: Kratos.ModelPart, arg1: float, arg2: float, arg3: bool) -> None: ...

class ContinuumExplicitSolverStrategy(ExplicitSolverStrategy):
    def __init__(self, arg0: ExplicitSolverSettings, arg1: float, arg2: int, arg3: float, arg4: int, arg5, arg6, arg7: Kratos.SpatialSearch, arg8: Kratos.Parameters) -> None: ...
    def ComputeCoordinationNumber(self, arg0: float) -> float: ...
    def RebuildListOfContinuumSphericParticles(self) -> None: ...

class ContinuumVelocityVerletSolverStrategy(ContinuumExplicitSolverStrategy):
    def __init__(self, arg0: ExplicitSolverSettings, arg1: float, arg2: float, arg3: float, arg4: int, arg5, arg6, arg7: Kratos.SpatialSearch, arg8: Kratos.Parameters) -> None: ...

class ControlModule2DProcess(Kratos.Process):
    def __init__(self, arg0: Kratos.ModelPart, arg1: Kratos.Parameters) -> None: ...

class DEMBeamConstitutiveLaw:
    def __init__(self) -> None: ...
    def CheckRequirementsOfStressTensor(self) -> bool: ...
    def Clone(self) -> DEMBeamConstitutiveLaw: ...
    def GetTypeOfLaw(self) -> str: ...
    def SetConstitutiveLawInProperties(self, arg0: Kratos.Properties, arg1: bool) -> None: ...

class DEMBeamConstitutiveLawPointerVariable:
    def __init__(self, *args, **kwargs) -> None: ...

class DEMContinuumConstitutiveLaw:
    def __init__(self) -> None: ...
    def CheckRequirementsOfStressTensor(self) -> bool: ...
    def Clone(self) -> DEMContinuumConstitutiveLaw: ...
    def GetTypeOfLaw(self) -> str: ...
    def SetConstitutiveLawInProperties(self, arg0: Kratos.Properties, arg1: bool) -> None: ...
    def SetConstitutiveLawInPropertiesWithParameters(self, arg0: Kratos.Properties, arg1: Kratos.Parameters, arg2: bool) -> None: ...

class DEMContinuumConstitutiveLawPointerVariable:
    def __init__(self, *args, **kwargs) -> None: ...

class DEMDiscontinuumConstitutiveLaw:
    def __init__(self) -> None: ...
    def Clone(self) -> DEMDiscontinuumConstitutiveLaw: ...
    def GetTypeOfLaw(self) -> str: ...
    def SetConstitutiveLawInProperties(self, arg0: Kratos.Properties, arg1: bool) -> None: ...

class DEMDiscontinuumConstitutiveLawPointerVariable:
    def __init__(self, *args, **kwargs) -> None: ...

class DEMFEMUtilities:
    def __init__(self) -> None: ...
    def CreateRigidFacesFromAllElements(self, arg0: Kratos.ModelPart, arg1: Kratos.Properties) -> None: ...
    def MoveAllMeshes(self, arg0: Kratos.ModelPart, arg1: float, arg2: float) -> None: ...

class DEMIntegrationScheme:
    def __init__(self) -> None: ...
    def SetRotationalIntegrationSchemeInProperties(self, arg0: Kratos.Properties, arg1: bool) -> None: ...
    def SetTranslationalIntegrationSchemeInProperties(self, arg0: Kratos.Properties, arg1: bool) -> None: ...

class DEMIntegrationSchemePointerVariable:
    def __init__(self, *args, **kwargs) -> None: ...

class DEMIntegrationSchemeRawPointerVariable:
    def __init__(self, *args, **kwargs) -> None: ...

class DEM_D_Bentonite_Colloid(DEMDiscontinuumConstitutiveLaw):
    def __init__(self) -> None: ...

class DEM_D_Conical_damage(DEMDiscontinuumConstitutiveLaw):
    def __init__(self) -> None: ...

class DEM_D_Hertz_confined(DEM_D_Hertz_viscous_Coulomb):
    def __init__(self) -> None: ...

class DEM_D_Hertz_viscous_Coulomb(DEMDiscontinuumConstitutiveLaw):
    def __init__(self) -> None: ...

class DEM_D_Hertz_viscous_Coulomb2D(DEM_D_Hertz_viscous_Coulomb):
    def __init__(self) -> None: ...

class DEM_D_Hertz_viscous_Coulomb_DMT(DEM_D_Hertz_viscous_Coulomb):
    def __init__(self) -> None: ...

class DEM_D_Hertz_viscous_Coulomb_JKR(DEM_D_Hertz_viscous_Coulomb):
    def __init__(self) -> None: ...

class DEM_D_Hertz_viscous_Coulomb_Nestle(DEM_D_Hertz_viscous_Coulomb):
    def __init__(self) -> None: ...

class DEM_D_Linear_Custom_Constants(DEM_D_Linear_viscous_Coulomb):
    def __init__(self) -> None: ...

class DEM_D_Linear_HighStiffness(DEMDiscontinuumConstitutiveLaw):
    def __init__(self) -> None: ...

class DEM_D_Linear_confined(DEM_D_Linear_viscous_Coulomb):
    def __init__(self) -> None: ...

class DEM_D_Linear_viscous_Coulomb(DEMDiscontinuumConstitutiveLaw):
    def __init__(self) -> None: ...

class DEM_D_Linear_viscous_Coulomb2D(DEM_D_Linear_viscous_Coulomb):
    def __init__(self) -> None: ...

class DEM_D_Linear_viscous_Coulomb_DMT(DEM_D_Linear_viscous_Coulomb):
    def __init__(self) -> None: ...

class DEM_D_Linear_viscous_Coulomb_JKR(DEM_D_Linear_viscous_Coulomb):
    def __init__(self) -> None: ...

class DEM_D_Stress_Dependent_Cohesive(DEMDiscontinuumConstitutiveLaw):
    def __init__(self) -> None: ...

class DEM_Dempack(DEMContinuumConstitutiveLaw):
    def __init__(self) -> None: ...

class DEM_Dempack2D(DEM_Dempack):
    def __init__(self) -> None: ...

class DEM_Dempack2D_dev(DEM_Dempack_dev):
    def __init__(self) -> None: ...

class DEM_Dempack_dev(DEM_Dempack):
    def __init__(self) -> None: ...

class DEM_Dempack_torque(DEM_Dempack):
    def __init__(self) -> None: ...

class DEM_ExponentialHC(DEMContinuumConstitutiveLaw):
    def __init__(self) -> None: ...

class DEM_FEM_Search:
    def __init__(self) -> None: ...
    def GetBBHighPoint(self) -> Kratos.Array3: ...
    def GetBBLowPoint(self) -> Kratos.Array3: ...

class DEM_Force_Based_Inlet(DEM_Inlet):
    @overload
    def __init__(self, arg0: Kratos.ModelPart, arg1: Kratos.Array3, arg2: int) -> None: ...
    @overload
    def __init__(self, arg0: Kratos.ModelPart, arg1: Kratos.Array3) -> None: ...

class DEM_Inlet:
    @overload
    def __init__(self, arg0: Kratos.ModelPart) -> None: ...
    @overload
    def __init__(self, arg0: Kratos.ModelPart, arg1: int) -> None: ...
    @overload
    def __init__(self, arg0: Kratos.ModelPart, arg1: Kratos.Parameters, arg2: int) -> None: ...
    def CreateElementsFromInletMesh(self, arg0: Kratos.ModelPart, arg1: Kratos.ModelPart, arg2: ParticleCreatorDestructor) -> None: ...
    def GetMaxRadius(self, arg0: Kratos.ModelPart) -> float: ...
    def GetTotalMassInjectedSoFar(self) -> float: ...
    def GetTotalNumberOfParticlesInjectedSoFar(self) -> int: ...
    def InitializeDEM_Inlet(self, model_part: Kratos.ModelPart, creator_destructor: ParticleCreatorDestructor, using_strategy_for_continuum: bool = ...) -> None: ...

class DEM_KDEM(DEMContinuumConstitutiveLaw):
    def __init__(self) -> None: ...

class DEM_KDEM2D(DEM_KDEM):
    def __init__(self) -> None: ...

class DEM_KDEMFabric(DEM_KDEM):
    def __init__(self) -> None: ...

class DEM_KDEMFabric2D(DEM_KDEM2D):
    def __init__(self) -> None: ...

class DEM_KDEM_CamClay(DEM_KDEM_Rankine):
    def __init__(self) -> None: ...

class DEM_KDEM_Fissured_Rock(DEM_KDEM_Rankine):
    def __init__(self) -> None: ...

class DEM_KDEM_Mohr_Coulomb(DEM_KDEM_Rankine):
    def __init__(self) -> None: ...

class DEM_KDEM_Rankine(DEM_KDEM):
    def __init__(self) -> None: ...

class DEM_KDEM_soft_torque(DEM_KDEM):
    def __init__(self) -> None: ...

class DEM_KDEM_soft_torque_with_noise(DEM_KDEM_soft_torque):
    def __init__(self) -> None: ...

class DEM_KDEM_with_damage(DEM_KDEM_soft_torque):
    def __init__(self) -> None: ...

class DEM_KDEM_with_damage_parallel_bond(DEM_KDEM_with_damage):
    def __init__(self) -> None: ...

class DEM_KDEM_with_damage_parallel_bond_2D(DEM_KDEM_with_damage_parallel_bond):
    def __init__(self) -> None: ...

class DEM_KDEM_with_damage_parallel_bond_Hertz(DEM_KDEM_with_damage_parallel_bond):
    def __init__(self) -> None: ...

class DEM_KDEM_with_damage_parallel_bond_capped(DEM_KDEM_with_damage_parallel_bond):
    def __init__(self) -> None: ...

class DemSearchUtilities:
    def __init__(self, arg0: Kratos.SpatialSearch) -> None: ...
    @overload
    def SearchNodeNeighboursDistances(self, arg0: Kratos.ModelPart, arg1: Kratos.ModelPart, arg2: float, arg3: Kratos.DoubleVariable) -> None: ...
    @overload
    def SearchNodeNeighboursDistances(self, arg0: Kratos.NodesArray, arg1: Kratos.ModelPart, arg2: float, arg3: Kratos.DoubleVariable) -> None: ...
    @overload
    def SearchNodeNeighboursDistances(self, arg0: Kratos.ModelPart, arg1: Kratos.NodesArray, arg2: float, arg3: Kratos.DoubleVariable) -> None: ...
    @overload
    def SearchNodeNeighboursDistances(self, arg0: Kratos.NodesArray, arg1: Kratos.NodesArray, arg2: float, arg3: Kratos.DoubleVariable) -> None: ...

class DiscreteRandomVariable(RandomVariable):
    @overload
    def __init__(self, arg0: Kratos.Parameters) -> None: ...
    @overload
    def __init__(self, arg0: Kratos.Parameters, arg1: int) -> None: ...
    def GetMean(self) -> float: ...
    def ProbabilityDensity(self, arg0: float) -> float: ...
    def Sample(self) -> float: ...

class DoubleList:
    def __init__(self) -> None: ...

class ExcavatorUtility:
    def __init__(self, arg0: Kratos.ModelPart, arg1: float, arg2: float, arg3: float, arg4: float, arg5: float, arg6: float, arg7: float, arg8: float, arg9: float, arg10: float, arg11: float, arg12: float, arg13: float) -> None: ...
    def ExecuteInitializeSolutionStep(self) -> None: ...

class ExplicitSolverSettings:
    cluster_model_part: Kratos.ModelPart
    contact_model_part: Kratos.ModelPart
    fem_model_part: Kratos.ModelPart
    inlet_model_part: Kratos.ModelPart
    r_model_part: Kratos.ModelPart
    def __init__(self) -> None: ...

class ExplicitSolverStrategy:
    def __init__(self, arg0: ExplicitSolverSettings, arg1: float, arg2: int, arg3: float, arg4: int, arg5, arg6, arg7: Kratos.SpatialSearch, arg8: Kratos.Parameters) -> None: ...
    def AttachSpheresToStickyWalls(self) -> None: ...
    def FinalizeSolutionStep(self) -> None: ...
    def Initialize(self) -> None: ...
    def InitializeSolutionStep(self) -> None: ...
    def PrepareContactElementsForPrinting(self) -> None: ...
    def PrepareElementsForPrinting(self) -> None: ...
    def RebuildListOfDiscontinuumSphericParticles(self) -> None: ...
    def ResetPrescribedMotionFlagsRespectingImposedDofs(self) -> None: ...
    def SearchDemNeighbours(self, arg0: Kratos.ModelPart, arg1: bool) -> None: ...
    def SearchFemNeighbours(self, arg0: Kratos.ModelPart, arg1: bool) -> None: ...
    def SetNormalRadiiOnAllParticles(self, arg0: Kratos.ModelPart) -> None: ...
    def SetSearchRadiiOnAllParticles(self, arg0: Kratos.ModelPart, arg1: float, arg2: float) -> None: ...
    def SetSearchRadiiWithFemOnAllParticles(self, arg0: Kratos.ModelPart, arg1: float, arg2: float) -> None: ...
    def SolveSolutionStep(self) -> float: ...

class ForwardEulerScheme(DEMIntegrationScheme):
    def __init__(self) -> None: ...

class IntList:
    def __init__(self) -> None: ...

class IterativeSolverStrategy(ExplicitSolverStrategy):
    def __init__(self, arg0: ExplicitSolverSettings, arg1: float, arg2: float, arg3: float, arg4: int, arg5, arg6, arg7: Kratos.SpatialSearch, arg8: Kratos.Parameters) -> None: ...

class KratosDEMApplication(Kratos.KratosApplication):
    def __init__(self) -> None: ...

class MoveMeshUtility:
    def __init__(self) -> None: ...
    def MoveDemMesh(self, arg0: Kratos.NodesArray, arg1: bool) -> None: ...

class MultiaxialControlModuleGeneralized2DUtilities:
    def __init__(self, arg0: Kratos.ModelPart, arg1: Kratos.ModelPart, arg2: Kratos.Parameters) -> None: ...
    def ExecuteFinalizeSolutionStep(self) -> None: ...
    def ExecuteInitialize(self) -> None: ...
    def ExecuteInitializeSolutionStep(self) -> None: ...

class OMP_DEMSearch(Kratos.SpatialSearch):
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, min_x: float, min_y: float, min_z: float, max_x: float, max_y: float, max_z: float) -> None: ...
    def SearchNodesInRadiusExclusive(self, arg0: Kratos.NodesArray, arg1: Kratos.NodesArray, arg2: list, arg3: VectorResultNodesContainer, arg4: VectorDistances, arg5: list, arg6: list) -> None: ...

class ParticleCreatorDestructor:
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, arg0: Kratos.Parameters) -> None: ...
    @overload
    def __init__(self, arg0) -> None: ...
    @overload
    def __init__(self, arg0, arg1: Kratos.Parameters) -> None: ...
    def CalculateSurroundingBoundingBox(self, arg0: Kratos.ModelPart, arg1: Kratos.ModelPart, arg2: Kratos.ModelPart, arg3: Kratos.ModelPart, arg4: float, arg5: bool) -> None: ...
    @overload
    def CreateSphericParticle(self, arg0: Kratos.ModelPart, arg1: int, arg2: Kratos.Array3, arg3: Kratos.Properties, arg4: float, arg5: Kratos.Element) -> Kratos.Element: ...
    @overload
    def CreateSphericParticle(self, arg0: Kratos.ModelPart, arg1: int, arg2: Kratos.Node, arg3: Kratos.Properties, arg4: float, arg5: Kratos.Element) -> Kratos.Element: ...
    @overload
    def CreateSphericParticle(self, arg0: Kratos.ModelPart, arg1: int, arg2: Kratos.Node, arg3: Kratos.Properties, arg4: float, arg5: str) -> Kratos.Element: ...
    @overload
    def CreateSphericParticle(self, arg0: Kratos.ModelPart, arg1: Kratos.Node, arg2: Kratos.Properties, arg3: float, arg4: str) -> Kratos.Element: ...
    @overload
    def CreateSphericParticle(self, arg0: Kratos.ModelPart, arg1: int, arg2: Kratos.Array3, arg3: Kratos.Properties, arg4: float, arg5: str) -> Kratos.Element: ...
    @overload
    def CreateSphericParticle(self, arg0: Kratos.ModelPart, arg1: Kratos.Array3, arg2: Kratos.Properties, arg3: float, arg4: str) -> Kratos.Element: ...
    def DestroyContactElementsOutsideBoundingBox(self, arg0: Kratos.ModelPart, arg1: Kratos.ModelPart) -> None: ...
    def DestroyMarkedParticles(self, arg0: Kratos.ModelPart) -> None: ...
    @overload
    def DestroyParticlesOutsideBoundingBox(self, arg0: Kratos.ModelPart) -> None: ...
    @overload
    def DestroyParticlesOutsideBoundingBox(self, arg0: Kratos.ModelPart) -> None: ...
    def FindMaxConditionIdInModelPart(self, arg0: Kratos.ModelPart) -> int: ...
    def FindMaxElementIdInModelPart(self, arg0: Kratos.ModelPart) -> int: ...
    def FindMaxNodeIdInModelPart(self, arg0: Kratos.ModelPart) -> int: ...
    def GetDiameter(self) -> float: ...
    def GetHighNode(self) -> Kratos.Array3: ...
    def GetLowNode(self) -> Kratos.Array3: ...
    @overload
    def MarkParticlesForErasingGivenBoundingBox(self, arg0: Kratos.ModelPart, arg1: Kratos.Array3, arg2: Kratos.Array3) -> None: ...
    @overload
    def MarkParticlesForErasingGivenBoundingBox(self, arg0: Kratos.ModelPart, arg1: Kratos.Array3, arg2: Kratos.Array3) -> None: ...
    def MarkParticlesForErasingGivenCylinder(self, arg0: Kratos.ModelPart, arg1: Kratos.Array3, arg2: Kratos.Array3, arg3: float) -> None: ...
    def MarkParticlesForErasingGivenScalarVariableValue(self, arg0: Kratos.ModelPart, arg1: Kratos.DoubleVariable, arg2: float, arg3: float) -> None: ...
    def MarkParticlesForErasingGivenVectorVariableModulus(self, arg0: Kratos.ModelPart, arg1: Kratos.Array1DVariable3, arg2: float, arg3: float) -> None: ...
    def RenumberElementIdsFromGivenValue(self, arg0: Kratos.ModelPart, arg1: int) -> None: ...
    def SetHighNode(self, arg0: Kratos.Array3) -> None: ...
    def SetLowNode(self, arg0: Kratos.Array3) -> None: ...
    def SetMaxNodeId(self, arg0: int) -> None: ...

class ParticlesHistoryWatcher(AnalyticWatcher):
    def __init__(self) -> None: ...
    def GetNewParticlesData(self, arg0: List[int], arg1: List[float], arg2: List[float], arg3: List[float], arg4: List[float], arg5: List[float]) -> None: ...

class PiecewiseLinearRandomVariable(RandomVariable):
    @overload
    def __init__(self, arg0: Kratos.Parameters) -> None: ...
    @overload
    def __init__(self, arg0: Kratos.Parameters, arg1: int) -> None: ...
    def GetMean(self) -> float: ...
    def ProbabilityDensity(self, arg0: float) -> float: ...
    def Sample(self) -> float: ...

class PostUtilities:
    def __init__(self) -> None: ...
    def AddModelPartToModelPart(self, arg0: Kratos.ModelPart, arg1: Kratos.ModelPart) -> None: ...
    def AddSpheresNotBelongingToClustersToMixModelPart(self, arg0: Kratos.ModelPart, arg1: Kratos.ModelPart) -> None: ...
    def ComputeEulerAngles(self, arg0: Kratos.ModelPart, arg1: Kratos.ModelPart) -> None: ...
    def ComputePoisson(self, arg0: Kratos.ModelPart) -> Kratos.Array3: ...
    def ComputePoisson2D(self, arg0: Kratos.ModelPart) -> Kratos.Array3: ...
    def IntegrationOfElasticForces(self, arg0: Kratos.NodesArray, arg1: Kratos.Array3) -> None: ...
    def IntegrationOfForces(self, arg0: Kratos.NodesArray, arg1: Kratos.Array3, arg2: Kratos.Array3, arg3: Kratos.Array3) -> None: ...
    def QuasiStaticAdimensionalNumber(self, arg0: Kratos.ModelPart, arg1: Kratos.ModelPart, arg2: Kratos.ProcessInfo) -> float: ...
    def VelocityTrap(self, arg0: Kratos.ModelPart, arg1: Kratos.Array3, arg2: Kratos.Array3) -> Kratos.Array3: ...

class PreUtilities:
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, arg0: Kratos.ModelPart) -> None: ...
    def ApplyConcentricForceOnParticles(self, arg0: Kratos.ModelPart, arg1: Kratos.Array3, arg2: float) -> None: ...
    def BreakBondUtility(self, arg0: Kratos.ModelPart) -> None: ...
    def CreateCartesianSpecimenMdpa(self, arg0: str) -> None: ...
    def FillAnalyticSubModelPartUtility(self, arg0: Kratos.ModelPart, arg1: Kratos.ModelPart) -> None: ...
    def MarkToEraseParticlesOutsideRadius(self, arg0: Kratos.ModelPart, arg1: float, arg2: Kratos.Array3, arg3: float) -> None: ...
    def MeasureBotHeigh(self, arg0: Kratos.ModelPart) -> list: ...
    def MeasureTopHeigh(self, arg0: Kratos.ModelPart) -> list: ...
    def PrintNumberOfNeighboursHistogram(self, arg0: Kratos.ModelPart, arg1: str) -> None: ...
    def ResetSkinParticles(self, arg0: Kratos.ModelPart) -> None: ...
    def SetClusterInformationInProperties(self, arg0: str, arg1: list, arg2: list, arg3: float, arg4: float, arg5: list, arg6: Kratos.Properties) -> None: ...
    def SetSkinParticlesInnerCircularBoundary(self, arg0: Kratos.ModelPart, arg1: float, arg2: float) -> None: ...
    def SetSkinParticlesOuterCircularBoundary(self, arg0: Kratos.ModelPart, arg1: float, arg2: float) -> None: ...
    def SetSkinParticlesOuterSquaredBoundary(self, arg0: Kratos.ModelPart, arg1: float, arg2: Kratos.Array3, arg3: float) -> None: ...

class PropertiesProxiesManager:
    def __init__(self) -> None: ...
    @overload
    def CreatePropertiesProxies(self, arg0: Kratos.ModelPart) -> None: ...
    @overload
    def CreatePropertiesProxies(self, arg0: Kratos.ModelPart, arg1: Kratos.ModelPart, arg2: Kratos.ModelPart) -> None: ...

class QuaternionIntegrationScheme(DEMIntegrationScheme):
    def __init__(self) -> None: ...

class RandomVariable:
    def __init__(self, arg0: Kratos.Parameters) -> None: ...
    def GetSupport(self, *args, **kwargs) -> Any: ...

class ReorderConsecutiveFromGivenIdsModelPartIO(Kratos.ReorderConsecutiveModelPartIO):
    @overload
    def __init__(self, arg0: str) -> None: ...
    @overload
    def __init__(self, arg0: str, arg1: int, arg2: int, arg3: int) -> None: ...
    @overload
    def __init__(self, arg0: str, arg1: int, arg2: int, arg3: int, arg4: Kratos.Flags) -> None: ...

class RungeKuttaScheme(DEMIntegrationScheme):
    def __init__(self) -> None: ...

class SphericElementGlobalPhysicsCalculator:
    def __init__(self, arg0: Kratos.ModelPart) -> None: ...
    def CalculateCenterOfMass(self, arg0: Kratos.ModelPart) -> Kratos.Array3: ...
    def CalculateD50(self, arg0: Kratos.ModelPart) -> float: ...
    def CalculateElasticEnergy(self, arg0: Kratos.ModelPart) -> float: ...
    def CalculateGravitationalPotentialEnergy(self, arg0: Kratos.ModelPart, arg1: Kratos.Array3) -> float: ...
    def CalculateInelasticFrictionalEnergy(self, arg0: Kratos.ModelPart) -> float: ...
    def CalculateInelasticViscodampingEnergy(self, arg0: Kratos.ModelPart) -> float: ...
    def CalculateMaxNodalVariable(self, arg0: Kratos.ModelPart, arg1: Kratos.DoubleVariable) -> float: ...
    def CalculateMinNodalVariable(self, arg0: Kratos.ModelPart, arg1: Kratos.DoubleVariable) -> float: ...
    def CalculateRotationalKinematicEnergy(self, arg0: Kratos.ModelPart) -> float: ...
    def CalculateSumOfInternalForces(self, arg0: Kratos.ModelPart) -> Kratos.Array3: ...
    def CalculateTotalMass(self, arg0: Kratos.ModelPart) -> float: ...
    def CalculateTotalMomentum(self, arg0: Kratos.ModelPart) -> Kratos.Array3: ...
    def CalculateTotalVolume(self, arg0: Kratos.ModelPart) -> float: ...
    def CalculateTranslationalKinematicEnergy(self, arg0: Kratos.ModelPart) -> float: ...
    def CalulateTotalAngularMomentum(self, arg0: Kratos.ModelPart) -> Kratos.Array3: ...
    def GetInitialCenterOfMass(self) -> Kratos.Array3: ...

class StationarityChecker:
    def __init__(self) -> None: ...
    def CheckIfItsTimeToChangeGravity(self, arg0: Kratos.ModelPart, arg1: float, arg2: float, arg3: float) -> bool: ...
    def CheckIfVariableIsNullInModelPart(self, arg0: Kratos.ModelPart, arg1: Kratos.DoubleVariable, arg2: float) -> bool: ...

class SymplecticEulerScheme(DEMIntegrationScheme):
    def __init__(self) -> None: ...

class TaylorScheme(DEMIntegrationScheme):
    def __init__(self) -> None: ...

class VectorDistances:
    def __init__(self) -> None: ...

class VectorResultNodesContainer:
    def __init__(self) -> None: ...

class VelocityVerletScheme(DEMIntegrationScheme):
    def __init__(self) -> None: ...

class VelocityVerletSolverStrategy(ExplicitSolverStrategy):
    def __init__(self, arg0: ExplicitSolverSettings, arg1: float, arg2: float, arg3: float, arg4: int, arg5, arg6, arg7: Kratos.SpatialSearch, arg8: Kratos.Parameters) -> None: ...
