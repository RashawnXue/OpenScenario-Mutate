AUTOMATIC_GEAR_TYPE = [
	'n', # Neutral position (N).
	'p', # Park position (P).
	'r', # Reverse position (R).
	'd', # Drive position (D).
]
CLOUD_STATE = [
	'cloudy', # Cloudy. There are more clouds than sunshine.
	'free', # Cloud free conditions.
	'overcast', # Overcast sky. Dull and gray looking.
	'rainy', # Rain clouds.
	'skyOff', # Turns off the sky visualization.
]
COLOR_TYPE = [
	'other', # Other (unspecified but known) color.
	'red', # Red color.
	'yellow', # Yellow color.
	'green', # Green color.
	'blue', # Blue color.
	'violet', # Violet color.
	'orange', # Orange color.
	'brown', # Brown color.
	'black', # Black color.
	'grey', # Grey color.
	'white', # White color.
]
CONDITION_EDGE = [
	'falling', # A condition defined with a falling edge shall return true at discrete time t if its logical expression is false at discrete time t and its logical expression was true at discrete time t-ts, where ts is the simulation sampling time.
	'none', # A condition defined with a 'none' edge shall return true at discrete time t if its logical expression is true at discrete time t.
	'rising', # A condition defined with a rising edge shall return true at discrete time t if its logical expression is true at discrete time t and its logical expression was false at discrete time t-ts, where ts is the simulation sampling time.
	'risingOrFalling', # A condition defined with a 'risingOrFalling' edge shall return true at discrete time t if its logical expression is true at discrete time t and its logical expression was false at discrete time t-ts OR if its logical expression is false at discrete time t and its logical expression was true at discrete time t-ts. ts is the simulation sampling time.
]
CONTROLLER_TYPE = [
	'lateral', # The controller can only affect in the lateral movement of the object.
	'longitudinal', # The controller can only affect in the longitudinal movement of the object.
	'lighting', # The controller can only affect the lighting of the object.
	'animation', # The controller can only affect an animation of the object.
	'movement', # The controller can affect both the lateral and longitudinal movement of the object (same as version 1.1).
	'appearance', # The controller can affect both the lighting and the animation of the object.
	'all', # The controller can affect all possible domains of the object.
]
COORDINATE_SYSTEM = [
	'entity', # Cartesian XYZ coordinate system (origin is the origin of the entity´s local coordinate system.)
	'lane', # Road-based s,t coordinate system (s-axis is the lane center line of the lane, on which the entity is located).
	'road', # Road-based s,t coordinate system (s-axis is the road center line of the road, on which the entity is located).
	'trajectory', # Trajectory-based s,t coordinate system (s-axis is the trajectory-arc, which the entity follows).
]
DIRECTIONAL_DIMENSION = [
	'longitudinal', # Longitudinal direction (along the x-axis).
	'lateral', # Lateral direction (along the y-axis).
	'vertical', # Vertical direction (along the z-axis).
]
DYNAMICS_DIMENSION = [
	'distance', # A predefined distance used to acquire the target value.
	'rate', # A predefined constant rate is used to acquire the target value.
	'time', # A predefined time (duration) is used to acquire the target value.
]
DYNAMICS_SHAPE = [
	'cubic', # Cubical transition f(x)=A*x^3+B*x^2+C*x+D with the constraint that the gradient must be zero at start and end.
	'linear', # Value changes in a linear function: f(x) = f_0 + rate * x.
	'sinusoidal', # Sinusoidal transition f(x)=A*sin(x)+B with the constraint that the gradient must be zero at start and end.
	'step', # The target value is set instantaneously. Does not consume simulation time.
]
FOLLOWING_MODE = [
	'follow', # Follow the lateral and/or longitudinal target value as good as possible by observing the dynamic constraints of the entity (e.g. for a driver model).
	'position', # Follow the trajectory, shape or profile exactly by ignoring the dynamic constraints of the entity.
]
FRACTIONAL_CLOUD_COVER = [
	'zeroOktas', # 0/8 of the sky is covered with clouds (equivalent to the deprecated 'free' CloudState)
	'oneOktas', # 1/8 of the sky is covered with clouds
	'twoOktas', # 2/8 of the sky is covered with clouds
	'threeOktas', # 3/8 of the sky is covered with clouds
	'fourOktas', # 4/8 of the sky is covered with clouds (equivalent to the deprecated 'cloudy' CloudState)
	'fiveOktas', # 5/8 of the sky is covered with clouds
	'sixOktas', # 6/8 of the sky is covered with clouds (equivalent to the deprecated 'rainy' CloudState)
	'sevenOktas', # 7/8 of the sky is covered with clouds
	'eightOktas', # 8/8 of the sky is covered with clouds (equivalent to the deprecated 'overcast' CloudState)
	'nineOktas', # sky obscured, e.g. in dense fog (equivalent to the deprecated 'skyOff' CloudState)
]
LATERAL_DISPLACEMENT = [
	'any', # Either left or right to the entity along the lateral dimension.
	'leftToReferencedEntity', # Left to the entity along the lateral dimension.
	'rightToReferencedEntity', # Right to the entity along the lateral dimension.
]
LIGHT_MODE = [
	'on', # Light is switched on.
	'off', # Light is switched off.
	'flashing', # Light is flashing. Therefore, flashingOnDuration and flashingOffDuration have to be set.
]
LONGITUDINAL_DISPLACEMENT = [
	'any', # Either ahead or behind the entity along the longitudinal dimension.
	'trailingReferencedEntity', # Behind the entity along the longitudinal dimension.
	'leadingReferencedEntity', # Ahead of the entity along the longitudinal dimension.
]
MISC_OBJECT_CATEGORY = [
	'barrier', # A barrier.
	'building', # A building.
	'crosswalk', # A crosswalk.
	'gantry', # A gantry.
	'none', # None, other
	'obstacle', # Not further defined obstacle
	'parkingSpace', # A parking space.
	'patch', # A patch.
	'pole', # A pole
	'railing', # A railing or guard rail.
	'roadMark', # Not further defined road mark.
	'soundBarrier', # A sound barrier.
	'streetLamp', # A street lamp.
	'trafficIsland', # A traffic island.
	'tree', # A tree
	'vegetation', # Not further defined vegetation.
	'wind', # Wind.
]
OBJECT_TYPE = [
	'miscellaneous', # Miscellaneous object.
	'pedestrian', # A Pedestrian.
	'vehicle', # A Vehicle.
	'external', # An external object reference.
]
PARAMETER_TYPE = [
	'boolean', # Boolean - true or false.
	'dateTime', # DateTime - Instant of time (Gregorian calendar).
	'double', # Double - IEEE 64-bit floating-point.
	'integer', # Integer (32-bit signed integer, equivalent to "int").
	'string', # String.
	'unsignedInt', # UnsignedInt - Unsigned integer of 32 bits.
	'unsignedShort', # UnsignedShort - Unsigned integer of 16 bits.
	'int', # Int - 32-bit signed integer.
]
PEDESTRIAN_CATEGORY = [
	'animal', # An animal.
	'pedestrian', # A pedestrian.
	'wheelchair', # A wheelchair.
]
PEDESTRIAN_GESTURE_TYPE = [
	'phoneCallRightHand', # Pedestrian is holding a phone in the right hand for a call.
	'phoneCallLeftHand', # Pedestrian is holding a phone in the left hand for a call.
	'phoneTextRightHand', # Pedestrian is holding a phone in the right hand for texting.
	'phoneTextLeftHand', # Pedestrian is holding a phone in the left hand for texting.
	'wavingRightArm', # Pedestrian is waving with the right arm.
	'wavingLeftArm', # Pedestrian is waving with the left arm.
	'umbrellaRightHand', # Pedestrian is holding a umbrella in the right hand.
	'umbrellaLeftHand', # Pedestrian is holding a umbrella in the left hand.
	'crossArms', # Pedestrian is crossing both arms.
	'coffeeRightHand', # Pedestrian is drinking a coffee with the right hand.
	'coffeeLeftHand', # Pedestrian is drinking a coffee with left hand.
	'sandwichRightHand', # Pedestrian is holding a sandwich with the right hand.
	'sandwichLeftHand', # Pedestrian is holding a sandwich with the left hand.
]
PEDESTRIAN_MOTION_TYPE = [
	'standing', # Pedestrian is standing.
	'sitting', # Pedestrian is sitting.
	'lying', # Pedestrian is lying down.
	'squatting', # Pedestrian is crouching/squatting.
	'walking', # Pedestrian is walking.
	'running', # Pedestrian is running.
	'reeling', # Pedestrian is reeling.
	'crawling', # Pedestrian is crawling.
	'cycling', # Pedestrian is cycling.
	'jumping', # Pedestrian is jumping.
	'ducking', # Pedestrian is ducking.
	'bendingDown', # Pedestrian is bending down.
]
PRECIPITATION_TYPE = [
	'dry', # No precipitation.
	'rain', # Rain.
	'snow', # Snow.
]
PRIORITY = [
	'overwrite', # If a starting event has priority Overwrite, all events in running state, within the same scope (maneuver) as the starting event, should be issued a stop command (stop transition).
	'override', # If a starting event has priority Override, all events in running state, within the same scope (maneuver) as the starting event, should be issued a stop command (stop transition).
	'parallel', # Execute in parallel to other events.
	'skip', # If a starting event has priority Skip, then it will not be ran if there is any other event in the same scope (maneuver) in the running state.
]
REFERENCE_CONTEXT = [
	'absolute', # Absolute reference.
	'relative', # Relative reference.
]
RELATIVE_DISTANCE_TYPE = [
	'lateral', # Smallest lateral distance (y for cartesian coordinate systems, t for road-based coordinate systems).
	'longitudinal', # Smallest longitudinal distance (x for cartesian coordinate systems, s for road-based coordinate systems).
	'cartesianDistance', # Cartesian distance offset. If used together with CoordinateSystem, then the value of the CoordinateSystem is not considered.
	'euclidianDistance', # Absolute magnitude of the euclidean distance vector. CoordinateSystem defaults to entity. If CoordinateSystem is defined by user, that value is overridden.
]
ROLE = [
	'none', # The entity has no specific role.
	'ambulance', # The entity role is ambulance.
	'civil', # The entity role is civil.
	'fire', # The entity role is fire fighting, e.g. fire engine.
	'military', # The entity role is military, e.g. camouflaged truck.
	'police', # The entity role is police.
	'publicTransport', # The entity role is public transport, e.g. a school bus.
	'roadAssistance', # The entity role is roadside assistance, e.g. tow truck.
]
ROUTE_STRATEGY = [
	'fastest', # Fastest route.
	'leastIntersections', # Route with least number of intersections.
	'random', # Random route.
	'shortest', # Shortest route.
]
ROUTING_ALGORITHM = [
	'assignedRoute', # Use the route which has already been assigned to the entity at the start position at the point in time when the distance shall be calculated.
	'fastest', # Calculate the route with the shortest travelling time between start and target position.
	'leastIntersections', # Calculate the route with as few junctions as possible between start and target position.
	'shortest', # Calculate the route with the shortest path between start and target position.
	'undefined', # It is up to the simulator how to calculate the route between the start and target positions.
]
RULE = [
	'equalTo', # 'Equal to' operator.
	'greaterThan', # 'Greater than' operator.
	'lessThan', # 'Less than' operator.
	'greaterOrEqual', # 'Greater or equal' operator.
	'lessOrEqual', # 'Less or equal' operator.
	'notEqualTo', # 'Not equal' operator.
]
SPEED_TARGET_VALUE_TYPE = [
	'delta', # The relative value is interpreted as a difference to a referenced value. Unit: [m/s]. As an example, a speed value of 10 equals a speed that's 10m/s faster than the reference speed.
	'factor', # The relative value is interpreted as a factor to a referenced value. No unit. As an example, a speed value of 1.1 equals a speed that's 10% faster than the reference speed.
]
STORYBOARD_ELEMENT_STATE = [
	'completeState', # State from which the Storyboard element cannot return to the running state without external interference (forced by a parent element).
	'endTransition', # Transition between the running state and the standby state. The moment the referenced StoryboardElement terminates its execution by completing its goal.
	'runningState', # State in which the storyboard element is executing its actions.
	'skipTransition', # Transition marking the moment an element is asked to move to the running state but is instead skipped so it remains in the standby state (Only for Event instances).
	'standbyState', # State in which the storyboard element could move to the running state given a start trigger.
	'startTransition', # Transition between the standby and running state. The moment the referenced StoryboardElement instance starts its execution.
	'stopTransition', # Transition between the running or standby states to the complete state. Occurs when the execution of the referenced StoryboardElement instance is stopped via a stop trigger or overriding.
]
STORYBOARD_ELEMENT_TYPE = [
	'act', # The referenced StoryboardElement instance is an Act.
	'action', # The referenced StoryboardElement instance is an Action.
	'event', # The referenced StoryboardElement instance is an Event.
	'maneuver', # The referenced StoryboardElement instance is a Maneuver.
	'maneuverGroup', # The referenced StoryboardElement instance is a ManeuverGroup.
	'story', # The referenced StoryboardElement instance is a Story.
]
TRIGGERING_ENTITIES_RULE = [
	'all', # All listed triggering entities must reach the specifies position in order to start the lane change.
	'any', # One of the triggering entities reaching the position is enough to trigger the lane change.
]
VEHICLE_CATEGORY = [
	'bicycle', # The vehicle is a bicycle.
	'bus', # The vehicle is a bus.
	'car', # The vehicle is a car.
	'motorbike', # The vehicle is a motor bike.
	'semitrailer', # The vehicle is a semi trailer.
	'trailer', # The vehicle is a trailer.
	'train', # The vehicle is a train.
	'tram', # The vehicle is a tram.
	'truck', # The vehicle is a truck.
	'van', # The vehicle is a van.
]
VEHICLE_COMPONENT_TYPE = [
	'hood', # Hood of a vehicle.
	'trunk', # Trunk of a vehicle.
	'doorFrontRight', # Front right door of a vehicle.
	'doorFrontLeft', # Front left door of a vehicle.
	'doorRearRight', # Rear right door of a vehicle.
	'doorRearLeft', # Rear left door of a vehicle.
	'windowFrontRight', # Front right window of a vehicle.
	'windowFrontLeft', # Front left window of a vehicle.
	'windowRearRight', # Rear right window of a vehicle.
	'windowRearLeft', # Rear left window of a vehicle.
	'sideMirrors', # All side mirrors of a vehicle.
	'sideMirrorRight', # All right side mirrors of a vehicle.
	'sideMirrorLeft', # All left side mirrors of a vehicle.
]
VEHICLE_LIGHT_TYPE = [
	'daytimeRunningLights', # Daytime running lights of a vehicle.
	'lowBeam', # Low beam of a vehicle.
	'highBeam', # High beam of a vehicle.
	'fogLights', # All fog lights of a vehicle.
	'fogLightsFront', # Front fog lights of a vehicle.
	'fogLightsRear', # Rear fog lights of a vehicle.
	'brakeLights', # Brake lights of a vehicle.
	'warningLights', # Warning lights of a vehicle.
	'indicatorLeft', # Left indicators of a vehicle.
	'indicatorRight', # Right indicators of a vehicle.
	'reversingLights', # Reversing lights of a vehicle.
	'licensePlateIllumination', # License plate illumination of a vehicle.
	'specialPurposeLights', # E.g. emergency light of a emergency-, police-, ... vehicle or service lights.
]
WETNESS = [
	'dry', # Not wet.
	'moist', # Wet but no puddles are formed.
	'wetWithPuddles', # Wet, puddles are formed.
	'lowFlooded', # Road completely covered with water. No puddles anymore.
	'highFlooded', # Road completely covered with water. Water depth > 5cm.
]

ENUM_TYPES = {
    'AutomaticGearType': AUTOMATIC_GEAR_TYPE,
    'CloudState': CLOUD_STATE,
    'ColorType': COLOR_TYPE,
    'ConditionEdge': CONDITION_EDGE,
    'ControllerType': CONTROLLER_TYPE,
    'CoordinateSystem': COORDINATE_SYSTEM,
    'DirectionalDimension': DIRECTIONAL_DIMENSION,
    'DynamicsDimension': DYNAMICS_DIMENSION,
    'DynamicsShape': DYNAMICS_SHAPE,
    'FollowingMode': FOLLOWING_MODE,
    'FractionalCloudCover': FRACTIONAL_CLOUD_COVER,
    'LateralDisplacement': LATERAL_DISPLACEMENT,
    'LightMode': LIGHT_MODE,
    'LongitudinalDisplacement': LONGITUDINAL_DISPLACEMENT,
    'MiscObjectCategory': MISC_OBJECT_CATEGORY,
    'ObjectType': OBJECT_TYPE,
    'ParameterType': PARAMETER_TYPE,
    'PedestrianCategory': PEDESTRIAN_CATEGORY,
    'PedestrianGestureType': PEDESTRIAN_GESTURE_TYPE,
    'PedestrianMotionType': PEDESTRIAN_MOTION_TYPE,
    'PrecipitationType': PRECIPITATION_TYPE,
    'Priority': PRIORITY,
    'ReferenceContext': REFERENCE_CONTEXT,
    'RelativeDistanceType': RELATIVE_DISTANCE_TYPE,
    'Role': ROLE,
    'RouteStrategy': ROUTE_STRATEGY,
    'RoutingAlgorithm': ROUTING_ALGORITHM,
    'Rule': RULE,
    'SpeedTargetValueType': SPEED_TARGET_VALUE_TYPE,
    'StoryboardElementState': STORYBOARD_ELEMENT_STATE,
    'StoryboardElementType': STORYBOARD_ELEMENT_TYPE,
    'TriggeringEntitiesRule': TRIGGERING_ENTITIES_RULE,
    'VehicleCategory': VEHICLE_CATEGORY,
    'VehicleComponentType': VEHICLE_COMPONENT_TYPE,
    'VehicleLightType': VEHICLE_LIGHT_TYPE,
    'Wetness': WETNESS
}
