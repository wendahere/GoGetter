This markdown file is used to record weekly progress for Grace Orchard School Vending Machine group. More details can be found in the meeting minutes.

## Week 0 (31/08/20 to 13/09/20)

On 02/09/2020 Meeting with project supervisor, Mr Soh for Project Kick Off, on Microsoft teams, at 19:40.

The budget was set to $1700. We settled admin matter. We were tasked to come up with questions to ask Grace Orchard School (GOS). Mr Soh preferred using more Robust programming such as micro PLC, rather than using Arduino which is less reliable. 

Final finishing to avoid being "Toy"-like (no wood), professional looking finishing.

Phase 1 / 2 - like at which phase the project should finish. We discussed and decided to aim to finish the project, not passing to next batch of students.

The purpose of the vending machine is to reward students for good behavior.

- Find out about the rules
- What are the prizes 
-They come in various forms, shapes and sizes
- Maybe it can be put inside a box?

**Things to ask GOS:**

- Can they standardise the shape/size of prizes
- How does the point system work?
- What do they envision the points identification system to be like
- Can we use RFID cards? Give cards to student to monitor points
- Do students already have cards/can we have several for testing
- Find out about the rules
- Is it okay to keep refilling often? 
- Rate of prizes being depleted (How long does it take to clear out prizes?)

**Programming**

- Do not want Arduino (Less reliable), rather Raspberry Pi
- Robust programming - micro plc 
- Try to get as cheap as possible 10 I/O
- Minimize sensors 
- Limit switches
- Able to buy from Sim Lim Tower
- Servo(Not in favor, less accuracy) or Stepper motor
- Once we firm up what parts we need, we can go search for prices of parts

**Hardware and build**

- Aluminium/mild steel Chassis (Find someone to weld for us)
- Avoid “Toy” like finishing, e.g. no wood 
-Professional looking
- Parts that vending machine companies have, we can ask for sponsor
- Shorten the height of the vending machine (budget constraints)
- Transparent panel for people to see through
- A system to dispense the prizes
- A system to identify the input (points accumulated by the students)
- Secure way of dispensing/storing the prizes
- Sensors 
- Scan stamps then dispense 
- QR code system?
- Vending machine dispensing mechanism
- Spiral type of vending machine
- Tray that holds many sizes (Complex..)


**CDIO process**

**Conceive:** 

- Find out what the customer wants, scope of project, limitation

**Design:**

- What you can do based on limitations. 
- Break product into many functions eg, delivery, display, security, 
- Calculations and CAD Design (With dimension drawn)
- Each function have many ideas and rank them, what you can do, ranking of ideas, calculations, cad (dimension drawings)
- Hunt for parts

**Implementation:**

- Fabrication and Testing

**Operation:** 

- Feedback, recommendation for maintenance Deliver the product and receive feedback from employer for improvement

**Bill of Material(BOM)**

- Determine number of parts, and ALL must be PROPERLY documented in the BOM
- Everything designed must have a number (part number) [in running order refer to BOM template]
- If product is simple enough do not need sub assembly
- Naming of parts/assembly must have structure (in running numerical order)
- If feeding tray is name SP1000, all affiliated parts will follow the 1000 series
- If using standard parts (fasteners/actuators) use the standard parts list and also put in - BOM (put it last in the BOM) [general names like ISO can put in brand/remarks]

**Concept Selection** (Be as objective as possible)

- Break our products into many functions (dispensing)
- For each function use the table given as a starting point
- A,B,C,D -> the different designs available
- A is the “control” basically reference, so use the GOS original “cabinet”
- Selection criteria: put 0 as the control, if the criteria is better than ori then use +, if otherwise use -, then need to count the number of + and -, to find nett score
- Weightage, if there is a tie for a particular function (refer to template)
- Can use pros/cons if we want to, but try to use the above 

**FYP report**

- Use roman numerals before actual content stuff
- Use arabic numbering for actual content stuff 
- Can use github
- Invite Mr Soh via email to let him check our progress

**What we should do now**

- Think of the functions of the vending machine (must have a few ideas for each function, 3 5 ideas?)
- Dispensing function
- Different designs
- Holding/storage function
- Secure
- Points identification/input function
- RFID, QR scanning
- Mobility function
- Wheels for transport

**On 05/09/2020, Team meeting 1**

We discussed team name, roles for each of us and what to do before Transdisciplinary Innovative Project(TIP) ends.  

**Team name/vending machine name**

- Prize Box
- Project Uppgradera
- Star Vendor
- Go-Getter
- Let’s give back together
- 
**Github/website**

- Wen Da - set up
- Do a group journal - progress can be shown by uploads (weekly updates on what we do) [do write-ups]
- Layout - format as we go (looks neat and simple)
- Website (html) - see if we wanna do or not 

**What to do before TIP ends**

- Each of us brainstorm design ideas for each function of the vending machine then throw all the ideas to the ideas section in the “MDP - Vending Machine” google docs
- Afterwards can find a time to do concept selection for each function (can do with Mr Soh) [narrow a few we can and want to do b4 we present to mr Soh]
- Don’t care about prices and practicality of the designs YET, just dump everything first then discuss during selection

**Software standardisation**
- Inventor professional 2021 [main designs/stress simulations]
- Rendering software - KIV
- Programming software - KIV
- Notepad++ [typing out our github]
- Microsoft onedrive 


**To do cad and then documentation there [DONE]**

- Machines to be used
- 3D printers from fablab 
- Metal sheet bending
- Welding (wenda settle)
- 2D CNC router
- Vacuum former

**Materials Acquisition**

- Find materials list required as early as possible to ask for sponsorship
- Even if we don’t need, we can have extra free stuff
- Vending Machine Casing (mild steel/carbon steel/stainless steel/aluminium)
- 3D printing filaments (for engineering stronk)
- Scrap metal for machining 
- Glass/ Clear Acrylic/ Plexiglass
- Wood
- Key/Locks
- Wheels (?)
- Vinyl Wrap/Paint
- Parts Acquisition
- PLC controllers
- Sensors
- Power Supply
- Vending Motor (?)
- LED (B)(no rgb)


## Week 1 (13/09/2020 to 19/09/2020) 

This week was our TIP week, thus we spent this week on research.

We did our preliminary research and consolidated our findings. 


**Things to consider**

- Ensure the core mechanism works well before adding fancy stuff
- Can Add machine learning to dictate which prizes the students can select from if project isn’t sufficiently complex
- Consider between stamp and rfid/nfc
- rfid/nfc has no visual feedback
- scanners/readers can be costly as a one-off
- Mobile phones can be used to write
- Stamp has physicality
- Detection of already used stamps
- Selection of number of stamps
- How can we make the product such that the organisation is able to use/service on their own
- App (if we are using RFID)
- Maintenance
- Restocking
- Redemption process
- Structure of vending machine
- Withstand wear
- Withstand weather elements
- Withstand vandalism*
- For aesthetic design, students to design signboard (“The Treasury”) and decide on colour scheme, the rest of the design left to us

**Ideas**

- Security function
- Electromagnetic lock (https://www.chinahao.com/product/533936921875/ )
- Use card to unlock
- Use biometrics to unlock
- Physical lock 
- Combi lock
- Deadbolt lock
- T-handle lock
- Padlock
- Door function
- Sliding door
- Swinging door
- Folding door
(Same as the ea classroom)
- Flip-up door
(Not feasible)

**Aesthetic function**
- Internal lighting
- LED
- Fluorescent
- External lighting
- LED 
- Fluorescent
- External designs
- Stickers
- Murals
- Paint
- Points identification/input function
- Using RFID Mifare Magic 1k 13.56MHz tech rather than 125kHz RFID, phones can read/write to 13.56MHz
- Machine learning to identify stamps on cards
- Punch card 
- Storage function
- Slide Rail Drawer (filing cabinet)
- Side-hung Drawer Slide


**Input function**

- 10 inch touch display screen, users can select choice of gift
- Display screen and separate buttons for controlling
- Button under each prizes
- Prize collection function
- Trap door outside
- Trap door inside
- No door
- Add a flap outside
- Sliding door
- Swinging door
- Electromagnetic door


**Class token dispensing function**

- Bag/tape together with the prize
- Dispense from a reservoir of tokens
- Digital tokens (put into NFC card)
- Prize cushioning function (KIV)
- Rubber
- Felt
- Metal
- Car carpet
- Air bed
- Prize dispensing function
- Conveyor belt system
- Hook type dispenser
- Use the spiral type (put into the coils)
- Use the spiral type (hook on the coils)
- Arm to grab
- Locker type (unlock the locker when given command)
- Those push out then slide into exit (similar to drink spiral out then slide into exit)
SImilar to 2D router, but horizontal, (see Keymaster), move arm to a box and grab/push prize out
- Wheel Type dispenser 


Other ideas:
	

- Able for students to turn the wheel physically 
- Only need servo to open close the door
- Spring loaded, dispenser



**Research on PLC vs Arduino/Raspi**

1. Arduino is an Embedded system which means the arduino board is fixed into the application and what code you enter into the arduino will be only executed.
2. PLC is not an embedded system, it will be fixed separately.

3. In Arduino code works for the one type of application only, if you want to execute an another work you need to change
4. In PLC wee need to select the type of application
5. PLC is used for heavy applications. (industries, automation systems like airplanes , car washer systems)
6. Arduino is used for smaller applications.
7. PLC has the ability to increase the capacity like number of i/o pins and etc but arduino doesn't.
8. If any component in an Arduino board fails we have to replace the entire board but in PLC there is the need only to change that module for instance if the power module in PLC is broken it can be replaced but it’s not possible in Arduino.



## Week 2 (20/09/2020 to 26/09/2020) 


### 24/09/2020 - Site visit 1 to GOS

We had a site visit to Grace Orchard School. Below are minutes of the meeting:

**Target Audience**

- Special needs students
- Mild intellectual disability (MID) IQ range 50 - 70
- ASD students (minority)
- Split into am(older) and pm(younger) classes
- Age group: 7 - 16 (max 18*)

**GOS’ wants/needs**

- Collect data of the redemption of prizes/rewards
- To evaluate what prizes are most popular and vice versa
- Point requirements can be changed/configured as and when GOS wants to 
- Fine with weekly replenishments 
- Vending machine operating at 80% capacity

**Security system**

- Prevent forgery of cards
- Secure storage function
- If using NFC cards
- Cards have their own digital footprint/identification
- Show their own history (accumulation/reduction of points for prize redemption)
- Visual feedback preferred
Tokens/coins for class system are dispensed together with the prizes
When students redeem experience based prizes (flag raising, prefect experience), teachers are to be informed

**Current treasury system**

- A lot of different stamps were used (colours/designs)
- Same value irregardless of designs/colours
- Pre-covid, treasury opened once a week, from first to last recess, two sessions, opened on Wednesdays
- Once prizes are redeemed, the card will be stamped/written over with “redeemed”
- Any excess points are transferred to the new card
- Students can keep the old card


**Redemption process (2 staffs)**
- Staff 1 (admin) - point deduction, issuance of new cards (if necessary)
- Staff 2 (security) - students show him their cards to see if eligible 
- Current cabinet is made of sheet metal, printed gold, with bulky decorations on top

**Reward system: Good Game, Grace Orchard (G2GO)**



1. Do task
2. Display good behaviour
3. Earn stamps
4. Teacher gives chopes as and when deemed appropriate by them
5. Claim Rewards


**Different tiers of rewards**

- Tier 1 is 40 pts, tier 2 is 70, tier 3 is 100
- There are prizes worth more than 100 pts, but not displayed in cabinet
- Principal club worth 500 pts

**Class system**

- Prizes redeemed from various tiers, would give students a number of tokens/coins, where the amount of tokens given corresponds to the tier of prizes redeemed from
- Class system prizes won’t be dispensed by the vending machine
- Experience based prizes are given in the form of a voucher
- They buy the cheapest prizes possible

**Things to note**

- 100 staff (each of them have a stamp at all times)
- 400 students
- Probably need spares of stamps/cards
- If still using stamps, GOS can change the background

**Current Treasury Size**

- 1800x1000x500mm
- Wire Length 1m ++ (Moving location)

**Things to do**

- Do Gantt Chart
- Proposal to GOS 2nd week of October 2020 (5/10/20 - 9/10/20)

## Week 3 (27/09/2020 to 03/10/2020) 

We did concept selection for functions followed by weighted concept selection on those functions that had multiple functions that were desirable. We ended up combining a few functions together.  We also went to visit shops selling mechanical parts during the weekend to further narrow down our concept selections.

### On 28/09/2020 - Team meeting 2 (10:00am)

Below is the explanation for selection criteria and explanation for each function.


## Concept selection


### Points identification Function

Identifying and tabulating the accumulated points of the students and issuance of leftover points (if necessary).

**Security**

- How easy it is to scam the system
- Ease of use (students)
- How easy it is for students to present the cards for point counting
- Ease of use (teachers)
- Issuance of points to the students

**Reliability**

- Longevity of cards
- Accuracy of point detection and tabulation
- Feeding of cards into machine should not jam
- Lifespan of components (nfc reader, led, camera)

**Implementability**

- How easy for us to change from the current system to the new system
- If we need to add in additional functions such as hole stamping mechanism, printer etc.

**Maintainability**

- How easy to keep the entire system running
- How easy for GOS to repair and upkeep

**Cost to implement**

- How much does it cost to change from the current system
- Component cost (camera, lights)
- Material costs
- Cost to operate (for GOS)
- Replacement of marking devices (stamps, hole punch)
- Replacement of cards (paper or plastic NFC cards)


**Issuance of replacement cards**

- How easy it is to issue cards with the calculated excess points
- Space required to build the system

## Input Function

- For students to select the prizes they want.
- Durability
- Whether it can resist being tampered with
- Physical impact
- Weather resistance	

**Ease of use**

- How easy it is for students to select a prize (User interface/experience)

**Reliability**

- Longevity of components
- Will it last in two years time?

**Maintenance**

- How easy it is for teachers to maintain the system
- Cost to replace/upkeep

**Implementability**

- How easy it is to implement
- Sensory Feedback
- System is able to tell users good job on earning the points etc


**Visual Feedback**

- Whether users can see how much points are left
- Cost 
- Cost to implement the system

**Prize Dispensing Function**

- The mechanism that dispenses/delivers the selected prizes

**Storage Volume**

- Number of prizes each chamber in the system can hold
- Variety of Prize
- Number of variety of prizes the system can dispense 
- Different shapes and sizes
- Empty Chamber Detection
- Whether system can determine if a prize slot is empty


**Reliability of components**

- Longevity of components
- Will it last in two years time?
- Will components break down/apart during operation
- Will the motors/gears jam/grind (Mechanical failure)
-Reliability of dispensing
- Whether prize will get stuck
- While dispensing
- While falling down
- Will the prizes break/get crushed
- While dispensing 
- While falling down


**Speed of Retrieval**

- Speed to dispense a prize


**Implementability**

- How easy it is to implement
- How much programming is required


**Ease of Replenishing**

- How easy it is for teachers to put new prizes
- Whether prepwork needs to be done before replenishing the prize


**User Experience for students**

- Experience of students when prize is being dispensed
- Fun factor when prize is being dispensed


**Maintainability**

- How easy it is for teachers to maintain the system
- Cost to replace/upkeep 
- Fix the system if failure occurs


**Cost**

- Cost to implement the system

## Prize Collection Function

The location in which the students reach out and retrieve/grab their dispensed prizes

**Security**

- Whether user can steal prizes


**Ease of use**

- How easy it is for users to collect the prizes
- Opening of doors
- Whether or not the collection point is intuitive (User-friendly)

**Reliability**

- Whether system will jam

**Longevity of components**

- Whether students can interfere with the sensors 
- Durability
- Longevity of components
- Will it last in two years time?
- Will the door get jammed?


**Safety**

- Will user get harmed when collecting prizes


**Maintainability**

- How easy it is for teachers to fix the collection function (eg door jammed)

**Implementability**

- How easy it is to implement 


**Feedback**

- Will users know if the prize has fallen down
- Audio or visual cue


**Cost**

- Cost to implement the system


## Token Dispensing Function

The mechanism that delivers the class tokens to students based on the level of prizes redeemed.

**Prepwork**

- How much prepwork is required to dispense the tokens

**Collection of token**

- How easy it is for students to collect the tokens
- Intuitiveness for token collection

**Reliability**

- Whether token will get stuck/lost
- Risk of giving out the wrong number of token

**Replensing**

- How easy it is for teachers to replenish the tokens

**Maintainability**

- How easy it is for teachers to fix the token dispensing function (token get stuck)

**Implementability**

- How easy it is to implement 

**Speed of Dispensing**

- Whether user has to wait for prize to be dispensed for token to be dispensed etc

**Cost**

- Cost to implement
- Cost to operate

## Security Function

How the door will stay closed.

**Ease of use**

- How easy it is for teachers to unlock and lock
- Any work is required prior (Registering biometric lock)

**Reliability**

- How reliable is the lock 
- During power failure

**Durability**

- How long the components can last
- Integrity of the lock

**Implementability**

- How easy it is to implemented

**Maintainability**

- How easy it is to fix the lock (due to tamper/wear and tear)
- How easy it is to replace the lock

**Security**

- Whether the lock can be tampered with/forced open
- Whether lock can be picked/code guessed
- Unauthorized opening
- Whether key can be lost

**Cost**

- Cost to implement/maintain

## Door Function

When the teacher opens the door to replenish the prizes.

**Safety**

- While opening will it hit anyone
- Pinch points (places where the finger will get stuck and injured/pinch)

**Ease of use**

- How easy to open/close the door
- How easy it is to leave the door open

**Reliability**

- How long can the door last without being replaced

**Durability**

- How the door can withstand wear and tear
- Whether the door can withstand physical impacts

**Maintainability**

- How easy it is to maintain/fix the door
- How easy it is to clean the window

**Implementability**

- How feasible is the fabrication of the door

**Cost**
- Cost to buy the door
- Cost of components (hinges etc)
- Cost to install the door

## Storage Function

The compartment where the dispensing mechanism is mounted/located.

**Storage size**

- How big it is
- Modularity
- Whether the storage can be modular
- Ability to preload the storage cartridge 
- How to integrate with the dispensing system

**Ease of use**

- Ease of accessing the dispensing system to replenish the prizes
- Structural integrity 
- Wear and tear (fatigue stress)
- Sturdiness (How solid it is)
- How much load it can take

**Maintainability**

- How easy it is to maintain/fix the storage function

**Safety**

- Whether the whole drawer will drop out

**Cost**

- Cost of maintenance
- Cost to buy components
- Cost to install


### Prototype to make (Before GOS Meeting) 
Decided functions (Please refer to concept selection excel)

- Points ID function - design B
- Input function - design C (backup D)
- Prize dispensing function - design E (backup B)
- Prize collection function - design C+D (backup E)
- Token dispensing function - design B (Tape and bag) 
- Security function -TBC
- Door function - design B
- Storage function - TBC

### 02/10/2020 - Team Meeting 3 (10:00am)

We had meeting with Mr Soh, our supervisor.

Most likely using PLC. Mdm Ho is familiar with the product. 
IA lecturer not familiar with that PLC. Can forget about the IOT component. 

Max is $1800 budget. 


**Gantt Chart** 

- No exam
- Specification is the main feature of product such as motor power, overall length, width, weight, dimensions, microprocessor etc.
-Material listing and Bill of Material
	- Material purchases is what we plan to buy
	- Material listing can ignore
- Fabrication procedure only required if fabrication in house, sub-contracted don't need to do, only need drawings

**Concept Selection**

- Name can change, once look at name must understand purpose
- Point Identification name has to change
- Input Function name don't like
- Prize collection function change to Collection Function 
- Prize Dispensing change to Dispensing Function
- Good to have sketches or images
- Can do sketches if pictures not clear for function images

**When pitching idea to stakeholder**

- Write simple write-up
- Do not explain everything to them 
- Do not have to show and explain concept selection
	- They are not interested
- Write up Interim report 
- Can do digital prototype first rather than physical prototype
- Selected functions should have clear picture in the presentation slides
- Describe feature by feature by combing through the prototype

**Description to explain why functions are rejected**

Can use concept selection ranking to say, low rank, thus reject.

Regarding Project Code, Mr Soh need to check his computer, will be given later
Next meeting should have some CAD to show overall idea

### Report

- Should write stakeholder names

**Methodology**

- Guided by CDIO framework
- Explain each CDIO meaning
	- C - to find out user need, what the team hope to develop
	- D - understand technical constraints, desirability of user and come up with technical features/product specs
	- I -  Fabrication of parts and testing of final product
	- O - Deliver product to stakeholder and receive feedback, construct user menu


**Conceiving the Project (2.1)**

- Mention, project initiated by GOS, field study was planned and based on findings the team start to ideate and come up with new ideas for subsequent designs

- Mention somewhere that we had project brief to come up with many concepts, outcome of research will be validated with field trip

**Regarding sponsorship**

- Tell them purpose of writing
- Doing good cause, completed artifacts will be given to this org
- Will appreciate if you donate some of parts to some of the projects
- Can put company logo on the frame as form of appreciation
- List down benefit for them


We can go straight to the D phase in CDIO. 

Start with calculations, some are to be done later, e.g. weight. Do power calculations. 
Can estimate force and benchmark based on current product. Size the bearings, must have housing for it, for easy mounting. 

Look at spiral mechanism, do they require bearing or cantilever. Can write to temasek foundation

**In 2 weeks time**
- Prepare an interim report, up to no. 2.5 in report 
- CAD structures to show full structure
- Current report can be used as an interim report 
- Do not need to have acknowledgment etc, straight to write up


By the next meeting, how many sensors do we need, and how many input and output do we require. Want to hear more on logic side, think that hardware side is okay.


**During weekends:**

Reynard: look into PLC, for more signal type (because we are bounded by number of I/O ports)

Wen Da: Look electrical portion, matrix wiring, how to get more out of the I/O ports, 
weekly journal 
try to find standard part for coils/lead screws, 
For matrix wiring, mosfet has to be used for negative side of wiring


Allen: Planning of design

All: Edit the report and insert images

## Field research

During the weekends, we went to hardware shops around 28 Kelantan Lane and around Blk 802 French Road to look at components and check prices.

For Threaded Rod/Lead screw, 10mm OD, 2mm approx $2.50 each, stainless steel $10.
Suggestion is to either cut into length and weld hexagon at one end or simply have a fixed nut in the frame to make the rod modular.

For springs, must be custom-made, 1 week lead time, approx $25 each, cost will go down for more quantity requested.

We also looked at hinges and drawer holder sliders etc.

Threaded Rod:
![Threaded ROd](https://raw.githubusercontent.com/wendahere/GoGetter/master/Images/25B71995-8C86-4A36-BA3B-5757B57D3372.jpg)

Springs:
![springs](https://raw.githubusercontent.com/wendahere/GoGetter/master/Images/30C7FAAF-4775-4331-92DD-76784193829B.jpg)

Drawer Slide:
![drawer slide](https://raw.githubusercontent.com/wendahere/GoGetter/master/Images/IMG_4947.JPG)

Hinges:
![hinges](https://raw.githubusercontent.com/wendahere/GoGetter/master/Images/1F619059-F7A6-46DF-B79C-113D8C1F0664.jpg)

## Week 4 (04/10/2020 to 10/10/2020) 

## Summary

Confirmed RaspberryPi as microcontroller. Finished cardboard prototype. Made a 12v to 5v voltage regulator. Talked to a company called ShiokPizza for sponsorship and to learn from their machines with a site visit. Meeting with Mr Soh on Friday.

### Monday 5/10/2020

After much discussion, we have decided to use a RasberryPi as the controller of our vending machine instead of a PLC, this is because given our limited budget, the PLC we could afford has too little I/O ports. Reynard has started working on the Pi. Allen has drawn some sketches of the design with concept sketches and a made a dirty prototype. Wen Da is working on the journal and will focus on the power calculations.

#### Concpet Sketches

Allen came up with some preliminary sketches on some of the main functions, so that the team have an idea how the final design would potentially look like. 

Layout planning for the vending machine:

<img src="https://raw.githubusercontent.com/wendahere/GoGetter/master/Images/Layout%20planning.jpg" alt="Layout planning" style="width:100%; height:100%;">

Different designs of the NFC card reader:
![Card reader](https://raw.githubusercontent.com/wendahere/GoGetter/master/Images/Card%20reader.jpg)
We decided to go with design 2.

Different views of the prize dispensing function:
![Dispensing](https://raw.githubusercontent.com/wendahere/GoGetter/master/Images/Dispensing.jpg)

![Dispensing 2](https://raw.githubusercontent.com/wendahere/GoGetter/master/Images/Dispensing%202.jpg) 

Prize collection function:
![Prize collection](https://raw.githubusercontent.com/wendahere/GoGetter/master/Images/Collection.jpg)

#### Dirty Prototype

A shoebox was used to make a dirty prototype of the vending machine, it helped to visualise where the different components will be located, and how will they be physically mounted on to the body of the vending machine. This is a quick, easy and inexpensive way for us to see whether the design ideas we decided during the conceive stage will be feasible.

Dirty prototype:

<img src="https://raw.githubusercontent.com/wendahere/GoGetter/master/Images/DP_external%201.jpg" alt="DP_external" width="49%"> <img src="https://raw.githubusercontent.com/wendahere/GoGetter/master/Images/DP_internals%20(empty).jpg" alt="DP_internals(empty)" width="49%">

<img src="https://raw.githubusercontent.com/wendahere/GoGetter/master/Images/DP_externalsC.jpg" alt="DP_externalsC"  width="49%"> <img src="https://raw.githubusercontent.com/wendahere/GoGetter/master/Images/DP_internalsC.jpg" alt="DP_internalsC" width="49%">

#### Door Design

After settling on a swinging door design, the team has to decide how many doors the vending machine will have. Looking at different vending machine designs, the most common designs are either a two door or a one door design. Seeing how we need to install a screen, keypad and NFC card reader/writer, we decided that a two door design fits best. One will be the main door that covers the storage and prize collection, we call that the main door; while the other door is where our inputs and screen will be installed on, we call that the I/O door. Having a separate I/O door means that the wiring for associated components will be easier as it does not need to go around the whole vending machine body, as compared to if a single door design is employed. To further make sense of this design, the dirty prototype is used, and it helped us to visualise where the potential wiring will be at. 

<img src="https://raw.githubusercontent.com/wendahere/GoGetter/master/Images/IO%20door%20wiring.jpg" width="50%">

From the image above, the blue line represents the different components we have on the I/O door, yellow refers to the microcontroller and its wiring, and green refers to our power supply unit. As we can see, it doesn't require much wire length to connect the microcontroller from the I/O door to the power supply unit.  

### Tuesday 6/10/2020
Allen used Inventor to draw out the 3D prototype. Wen Da did circuit drawings. 

#### Power supply

We decided to use a Power Supply Unit (PSU), rated AC input 220v +-15%, DC Output 12v, 15A. Since the RaspberryPi only requires 5v and about 2A max input, we are able to step down the 12V to 5V using a 7805 transistor. We are also putting a fuse at 12v (from PSU) side connected to the stepper motor driver. There is no fuse at the 5v RaspberryPi as the fuse has an extremely low chance to be blown. We are also putting capacitor in parallel at 12v and 5v from the PSU. We are using 24v rated capacitor at the 12v side and 10v rated capacitor at the 5v side. It is standard practice to double the capacitor size of voltage required.

Below is image of circuit sketch.
![sketch](https://raw.githubusercontent.com/wendahere/GoGetter/master/Images/circuit%20sketch.JPG)

Image of PSU we are using:
![PSU](https://raw.githubusercontent.com/wendahere/GoGetter/master/Images/psu3.JPG)

#### Dispensing mechanism

After doing further research, we decided to move our focus away from springs for the dispensing mechanism. This is because, we have found out that the springs we need have to be custom manufcatured, which means that they are expensive and not easily obtainable. We didn't want this as we wanted the standard parts that could be easily bought off the shelf, and require little to zero adjustments/machining. This is so, if any part fail during operation, GOS could easily maintain the machines by themselves, by ordering a replacement part online and replacing said part. Therefore, instead of using springs, we decided to switch to either using a threaded rod or lead screw driven by a stepper motor to dispense the prize instead. It still keeps the original design concept (prizes are hooked onto a rod). We also found that it will be easier for GOS to maintain the machine in the long run. Furthermore, the overall cost would be cheaper too.

However, to implement this design, GOS has to compromise, which is to pack the prizes into a bag, and tie it with a string that has a loop at the end, which will be hooked onto the lead screw or threaded rod to be dispensed. The reason why this step is necessary, it's because the threads on the rod are thin and narrow, and if a hook is used, the prizes will easily slide off the rod, should anyone rock and shake the vending machine. Fortunately, this wouldn't be too much additional work for GOS, as they will also need to include the class tokens with the prizes as well. 

As we decided to use lead screw/threaded rod for our dispensing mechanism, we needed to know how the mechanism would work. After conducting some research, we came out with 3 designs.

- Design 1: Connecting the lead screw/threaded rod to stepper motor using a coupling
	- ![Design 1](https://raw.githubusercontent.com/wendahere/GoGetter/master/Images/Design%201.jpg)
	- To connect 2 shafts together with a coupling, the connecting end of the shafts normally needs to be machined flat so that there is enough surface area for the set screw in the coupling to tightly secure the shafts to it
	-  However we do not want to do any additional machining because it wouldn't be easy for GOS to replicate the process, and we want the maintainence for them to be as easy as possible
	-  There could be a potential issue if we just connect the lead screw/threaded rod to the coupling directly, as  the set screw in the coupling may not have enough points of contact with the threads of the lead screw/threaded rod, and without enough grip, the connection may come lose in the future due to continuous rotation and vibration of the motor
	-  This happens to be the cheapest option compared to the other two
- Design 2: Use a stepper motor that comes installed with a lead screw  
	- ![Design 2](https://raw.githubusercontent.com/wendahere/GoGetter/master/Images/Design%202.jpg)
	- This design is the easiest to implement, as there is already a lead screw in the stepper motor, the motor just needs to be secured to a housing
	- Unfortunately, this kind of stepper motor is expensive, and given our limited budget, we will not be able to afford much motors, thus limiting the variety of prizes that will be dispensed
- Design 3: Using 2 gears, a driving gear connected to the stepper motor, and a driven gear connected to the lead screw/ threaded rod
	- ![Design 3](https://raw.githubusercontent.com/wendahere/GoGetter/master/Images/Design%203.jpg)
	- This design requires a specially made housing to attach the two gears
	- A problem with this design is that overtime, the gear tooth will experience wear and tear, and eventually some teeth will get worn down making some parts of the gears not able to mesh well together
	- With this design, there isn't much of a worry that the lead screw/threaded rod will come off easily during operation

Allen approached Mr Edward Tay, a SP lecturer who mainly teaches the practical lessons of design and build, a year 2 mechanical engineering module, to consult about the three designs for our dispensing mechanism.

For designs 1 and 3, there is the issue of alignment; fortunately for design 1, the use of flexible couplings should compensate any slight misalignments. However, for design 3, the same couldn't be said, because the pitch distance between the driver and driver gear must be carefully calculated to ensure that the teeth of the gears always needs to be engaged with each other to ensure accurate rotation of the lead screw/threaded rod when dispensing. The gear housings need to be manufactured one at a time so there's a chance that the holes for the gears might not be in the same location for each gear housing. Hence, it would take up a lot of time for the manufacture of gear housings if we proceed with design 3.

Mr Edward suggested that if we were to proceed with design 1, there's a way to mitigate the problem of the set screws of the coupling from coming loose due to vibration of the motor. The solution is to stack another screw onto the first screw. This way, it ensures that if the first screw actually comes loose during operation, the second screw is able to prevent it from further unfasten itself. Moreover, if we really want to ensure the screws does not come off, we apply some epoxy to further secure the screws to the coupling. 

Stacking screws:
<img src="https://raw.githubusercontent.com/wendahere/GoGetter/master/Images/Stacking%20screws.jpg" alt="stacking screws">

After taking the three designs into careful consideration, we decided that we would proceed with design 1. Firstly, it is the most economical option out of the three, as we only need stepper motors, couplings, and lead screws/threaded rods. Secondly, it can be easily aligned with the use of flexible couplings, moreover, alignment is not really critical for this function. Thirdly, accurate control of the dispensing motion can be achieved, since the lead scew/threaded rod is installed coaxially to the stepper motor, there is no concern of the gear teeth skipping.

![Dispensing assembly](https://raw.githubusercontent.com/wendahere/GoGetter/master/Images/Dispensing%20assembly.jpg) 
Thus the above shows a sketch of the final deisgn for the dispensing mechanism, a lead screw/threaded rod attached to a stepper motor with a coupling installed onto the storage component as a cantilever and supported by a bearing in a bearing bracket.

#### Prototype

After finalising what the designs for each function are. We needed to build a prototype and showcase it to GOS, showing them how the final design of the vending machine will look like. This is an important stage, because it is the final stage before we proceed to the final design stage, which includes calculations and material sourcing. Hence, any feedback from them is needed. Some feedback we are looking for are:

1. How user friendly the vending machine is for the staff to operate and for the students to interact?
2. Do they like the design?  
3. What are some of the pain points that a staff or student may experience?
4. What other additions to the machine do they want?
5. Are the compromises acceptable? (needing them to prepare the prizes beforehand)

The materials that we will mainly be using to build the prototype consists of corugated cardboard (single ply and double ply), PLA 3D printed parts, door hinges, fasteners (scews and nuts), acrylic, paper, and transparency.

#### 3D CAD 

Allen did the CAD drawings for the prototype in Inventor.  

**Body**

<img src="https://raw.githubusercontent.com/wendahere/GoGetter/master/Images/3D%20body%20wireframe.jpg" alt="3D body wireframe" width="49%"> <img src="https://raw.githubusercontent.com/wendahere/GoGetter/master/Images/3D%20body.png" alt="3D body" width="49%"> 
With reference to the diagram on the right, it shows the body of the vending machine. It is split into to compartments, the first compartment houses the dispensing mechanism, storage, and prize collection point, it is covered by the main door, while the other compartment houses all the electrical components, such as wires from the IO door and stepper motors in the dispensing mechanisms, power supply unit, it can also be used to store any specialised tools used to service the vending machine or any spare parts and act as a temporary storage for prizes as well, it is covered by the IO door, where the lock will also be installed on.  

With refernce to the diagram on the left, we can see four blue arrows each pointing at the same extruded features with an array of holes. These features are for us to mount the "slide rails" so that the storage of the dispensing mechanism can slide in and out like a drawer. It is designed this way to emulate what GOS staff will do when they need to replenish the prizes or perform any maintainence work. They can just slide out the dispensing mechansim storage in question, do the relevant work, and slide it back in. There are many holes there because we wanted to show that they have the option to change how far apart they want each storage to be, as some prizes may require a larger space to store. 

**Slide rail**

![Slide rail](https://raw.githubusercontent.com/wendahere/GoGetter/master/Images/Slide%20rail.png)
This is one part of the slide rail that is mounted onto the body using bolts and nuts through the holes.

![Slide rail A](https://raw.githubusercontent.com/wendahere/GoGetter/master/Images/Slide%20rail%20A.png)
This shows how it would look like when the slide rail is mounted onto the body. 

**Storage**

![Dispensing storage](https://raw.githubusercontent.com/wendahere/GoGetter/master/Images/Dispensing%20storage.png)
The holes in the storage component are to mount the motor and bearing brackets on it. While the part pointed by the red arrows are the second part of the slide rail that when we put the storage component on top of the first part of the slide rail, it can easily slide in and out like a drawer.

The part that is pointed by the green arrow serves two purposes. One, it acts as a handle for the staff to grab on, so they can pull the storage out and push it back in. Two, item tags can be put onto it to specify which motor dispenses what item, so that users know what number they should enter on the keypad in order to get their desired prize.

**Dispensing Mechanism**

![Dispensing mech](https://raw.githubusercontent.com/wendahere/GoGetter/master/Images/Dispensing%20mech.png)

The above shows the assembly of the dispensing mechanism. The motor and bearing brackets were designed by reynard. The purpose of the motor bracket is to act as a fixture for us to mount our stepper motor on, so that during operation, the motor stays in one place and doesn't shift out of place. While the purpose of the bearing bracket is to house a bearing that would take the rotational load of the lead screw during operation, this is because we do not want the coupling to be taking that load since as the coupling is only needed connect the lead screw/threaded rod to the steper motor shaft.

Motor Bracket: 

<img src="https://raw.githubusercontent.com/wendahere/GoGetter/master/Images/Motor%20bracket%20back.png" alt="motor bracket back" width="49%"> <img src="https://raw.githubusercontent.com/wendahere/GoGetter/master/Images/Motor%20bracket%20front.png" alt="motor bracket front" width="49%">

Bearing Bracket: 

![Bearing bracket](https://raw.githubusercontent.com/wendahere/GoGetter/master/Images/Bearing%20bracket.png)

Assembly of the dispensing mechanism on the storage component:
 
![Dispensing assembly](https://raw.githubusercontent.com/wendahere/GoGetter/master/Images/Dispensing%20assembly.png)
For this prototype, each storage compartment comprises of three dispensing mechanisms. Since there are three level of prizes, the prototype can holp up to 9 different prizes at a time. If GOS is happy with this implementation, for the final product we can proceed with it, but if our budget allows it and GOS requires more variety of prizes being dispensed, we can further expand it for the final product.

**Collection point**

The main purpose of the collection function is a place for the prizes to fall onto, so that students know where to claim them. It needs to be easily accessed and be able to prevent theft. Generally, most vending machines uses a internal trap door system that flips up when the outside flap is open, this allows for users to take their dispensed item but prevents them from reaching into the machine to take the other contents of the vending machine. There are also some other vending machines that uses a conveyor belt system that carries the dispensed item to a different collection point situated at the side of the machine rather than near the bottom of the machine commonly found in many vending machines in the market. 

For our design, we will just have a flap on the outside that is connected to a inner trapdoor that closes and opens. Speaking of the flap on the outside, we have to decide whether we want it the flap to be pushed open or pulled open. Generally, most vending machines' flaps are pushed open, but we found out that the flap normally scrapes on our arm when we forget to hold it open while we collect our items. We are worried that if students are not careful they might injure themselves which is the last thing we want our machine to cause. Therefore, we decided that the flap should be pulled open instead. This way, it is more intuitive to students that the door needs to be held open in order to collect the prizes.

Another thing to consider is where should the collection point be located at, either attached to the door, or installed in the body of the vending machine. We decided that the collection point will be installed in the body as if we wanted to add any electronics such as a drop sensor to the collection point, it is easier for us and the wiring will be neater as well. 

Collection point design: 

![CP O](https://raw.githubusercontent.com/wendahere/GoGetter/master/Images/CP%20O.png)
The above is the design we came up with, an inner flap is attached onto a hinge, which is then attached to a "wall". The space in between the "wall" to the door will be where the prize will drop into. How the inner flap works is it will be conencted using linkages to an outer flap which is attached to the door. As long the outer flap remains closed, the inner flap remains open, when a prize is dispensed and a prize drops, a student will pull open the outer flap in order to reach in to grab their prize, by doing so, the pulling motion of the front door will cause the inner flap to flip up and "close", hence preventing the student from reaching into to take anything else in the vending machine.

<img src="https://raw.githubusercontent.com/wendahere/GoGetter/master/Images/CP%20Old.png" alt="CP Old" width="537">
The "wall" alongside flap and hinge is installed into the body of the vending machine. It will be secured by screws and nuts.

Linkage design:

![Linkage O](https://raw.githubusercontent.com/wendahere/GoGetter/master/Images/Linkage%20O.png)
To conenct the motion of the outer flap to that of the inner flap, a three bar linkage is used. 

Linkage assembly to "wall":

![Collection point A O](https://raw.githubusercontent.com/wendahere/GoGetter/master/Images/Collection%20point%20A%20O.png) 
As we can see from above, the flap in front will be connected to the front door using a hinge.

**Main door**

![Main door O](https://raw.githubusercontent.com/wendahere/GoGetter/master/Images/Main%20door%20O.png)

For the design of the main door, it has 2 main cut outs. The bigger one will be covered with a sheet of transparency. The smaller cut out below is where the pull flap will be attached to.

**IO door**

![IO door O](https://raw.githubusercontent.com/wendahere/GoGetter/master/Images/IO%20door%20O.png)

The display screen, NFC reader and keypad will be located at the IO door. For this prototype, we will be using Wen Da's phone as the dusplay screen, and a custom made keypad with mechanical key switches, while we won't be putting any NFC reader on the door, there will be a holder for a card to be slotted onto,                 

### Wednesday 7/10/2020
Allen and Reynard worked together to laser cut and 3D print to fabricate first prototype.
Wen Da worked more on circuit. We tested the 7805 transistor using a power supply to check that it is working. Wen Da soldered the working 7805 on a copper stripboard with red and black wires to connect the PSU to the RaspberryPi. 

We are considering on using a Single Pole Double Throw Relay to reduce the amounts of stepper motor drivers required to cut down on cost.

This is how the circuit will look like:

![](https://raw.githubusercontent.com/wendahere/GoGetter/master/Images/SPDT.JPG)

Testing of 7805 transistor (12v from power supply step down to 5v)
![transtest](https://raw.githubusercontent.com/wendahere/GoGetter/master/Images/transistortest.PNG)

Soldered Stripboard

<img src="https://raw.githubusercontent.com/wendahere/GoGetter/master/Images/stripboard.JPG" alt="soldered stripboard" width="577" height="262">

#### Making the prototype

After everything has been CAD out by Allen, we proceeded to prepare the materials to build the prototype. We laser cut double and single ply cardboards.

![](https://raw.githubusercontent.com/wendahere/GoGetter/master/Images/Everything.JPG)

**Assembly**

<img src="https://raw.githubusercontent.com/wendahere/GoGetter/master/Images/A1.JPG" alt="A1" width="49%"> <img src="https://raw.githubusercontent.com/wendahere/GoGetter/master/Images/A2.JPG" alt="A2" width="49%"> The mounting panels are glued onto the left and middle walls of the body. The mounting panels are for us to attach one part of the slide rails.

<img src="https://raw.githubusercontent.com/wendahere/GoGetter/master/Images/A3.JPG" alt="A3">
Hinges are attached to the left and right walls of the body.

<img src="https://raw.githubusercontent.com/wendahere/GoGetter/master/Images/A4.JPG" alt="A4" width="49%"> <img src="https://raw.githubusercontent.com/wendahere/GoGetter/master/Images/A5.JPG" alt="A5" width="49%"> <img src="https://raw.githubusercontent.com/wendahere/GoGetter/master/Images/A6.JPG" alt="A6" width="49%"> <img src="https://raw.githubusercontent.com/wendahere/GoGetter/master/Images/A7.JPG" alt="A7" width="49%">
The right *(top left)*, back *(top right)*, middle *(bottom left)*, and right *(bottom right)* walls are glued to the base of the body. 

<img src="https://raw.githubusercontent.com/wendahere/GoGetter/master/Images/SR.JPG" alt="SR" width="49%"> <img src="https://raw.githubusercontent.com/wendahere/GoGetter/master/Images/A8.JPG" alt="A8" width="49%">
One pair of the slide rails is glued together *(left)*, and is mounted onto the mounting rails of the body with screws and nuts *(right)*.

<img src="https://raw.githubusercontent.com/wendahere/GoGetter/master/Images/S%20A1.JPG" alt="S A1" width="49%"> <img src="https://raw.githubusercontent.com/wendahere/GoGetter/master/Images/S%20A2.JPG" alt="S A2" width="49%">
The other pair of slide rails for the storage component is also glued together *(left)*. For back wall of the storage component is also glued to the base of the storage component *(right)*.

![S A3](https://raw.githubusercontent.com/wendahere/GoGetter/master/Images/S%20A3.JPG)
The slide rails is then glued to the base.

<img src="https://raw.githubusercontent.com/wendahere/GoGetter/master/Images/Handle.jpg" alt="Handle" width="49%"> <img src="https://raw.githubusercontent.com/wendahere/GoGetter/master/Images/Handle%20A.jpg" alt="Handle A" width="49%">
The handle is glued and assembled *(left)*, which is then glued onto the front of the storage component *(right)*. 

<img src="https://raw.githubusercontent.com/wendahere/GoGetter/master/Images/Masking%201.JPG" alt="Masking 1" width="49%"> <img src="https://raw.githubusercontent.com/wendahere/GoGetter/master/Images/Masking%202.jpg" alt="Masking 2" width="49%">
To ensure the storage component slides smoothly on the slide rail that is mounted on the body, we applied masking tape on the surfaces that comes into contact with each other when it slides in and out.

![Dipsensing mech A](https://raw.githubusercontent.com/wendahere/GoGetter/master/Images/Dispensing%20mech%20A.jpg)
The 3D printed parts are assembled next. A bearing is inserted in the bearing bracket *(purple)*; the stepper motor is attached to the motor bracket *(white)*, then they are installed onto the storage component using screws and nuts. The threaded motor is joined to the shaft of the stepper motor with the use of a flexible coupling. The assembly of the dispensing mechanism is now complete.

![Sliding](https://raw.githubusercontent.com/wendahere/GoGetter/master/Images/Sliding.jpg)
The storage component can be put into the body by sliding it down the slide rail that was previosuly installed on the body.

<img src="https://raw.githubusercontent.com/wendahere/GoGetter/master/Images/Transparency.jpg" alt="Transparency" width="49.5%"> <img src="https://raw.githubusercontent.com/wendahere/GoGetter/master/Images/Item%20tag.jpg" alt="Item tag" width="49.5%">
A sheet of transparency is folded into the shape as shown *(left)*. This will be covered on the front part of the storage component so that we can put in the item tags to indicate which stepper motor dispenses which item *(right)*. 

<img src="https://raw.githubusercontent.com/wendahere/GoGetter/master/Images/OCP1.JPG" alt="OCP1" width="49.5%"> <img src="https://raw.githubusercontent.com/wendahere/GoGetter/master/Images/OCP2.JPG" alt="OCP2" width="49.5%"> <img src="https://raw.githubusercontent.com/wendahere/GoGetter/master/Images/OCP3.JPG" alt="OCP3" width="49.5%"> <img src="https://raw.githubusercontent.com/wendahere/GoGetter/master/Images/OCP4.JPG" alt="OCP4" width="49.5%">
For the collection point, the collection "wall" is folded, a hinge is attached to the inner flap which is then attached to the collection "wall".

However, while we tried to install it to the body we realised that this design had a major flaw. If we attached the linkages to both the inner flap that is attached to the collection "wall" and the pull flap which is attached to the main door, we will not be able to open the main door at all. As a result of this oversight, we did not continue assembling the rest of the components, so that Allen can make the necessary design changes, and also check if any of the remaining designs require any amendments.

### Thursday 8/10/2020

Wen Da drew out circuit diagram for having Double Pole, Double Throw Relay (DPDT). After much consultation with electrical experts, we decided to use one fuse (about 10-12A) after the PSU steps down from 220v to 12v. This is because there is a fuse at the plug for the PSU. After stepping down, only 1 fuse is required. There is no need for each stepper motor to have it's own fuse. Afterwards, Wen Da went Sim Lim Tower to buy fuse holder, fuses and 4 pin wire. Wen Da also sent out emails for sponsorships.

![](https://raw.githubusercontent.com/wendahere/GoGetter/master/Images/WithDPDT.JPG)

#### Sponsorships
As the allocated funds for our project is limited, we needed to be resourceful 
Wen Da sent out more sponsorship emails.

#### Testing the stepper motor

We used Arduino to test the stepper motor as the Pi was very difficult and required more time. We followed this site 
[https://howtomechatronics.com/tutorials/arduino/how-to-control-stepper-motor-with-a4988-driver-and-arduino/](https://howtomechatronics.com/tutorials/arduino/how-to-control-stepper-motor-with-a4988-driver-and-arduino/ "Guide Link")

![aa](https://raw.githubusercontent.com/wendahere/GoGetter/master/Images/teststepper.JPG)

The circuit worked well initially but then white smoke starting to form near the motor driver. It turned out that the capacitor was placed in the wrong polarity. The capacitor was burnt, this was checked by using a Digital Multimeter, setting to resistance and having 0 resistance showed that the capacitor is burnt.

After changing the capacitor, the stepper is moving accordingly to the code. We measured the amperage of the entire circuit. This was done by setting the Multimeter to ampere and putting the pins parallel to the power supply. The total draw was 1.25mA. The current draw from the A4988 stepper driver is 0.38mA. However, the draw from the stepper motor is not 12.5mA minus 0.38mA as there was no load on the stepper while it was operating. In order to find out the max current draw, we have to put on the max load required.

After installing the threaded road (load), we tested the current draw and it was the same. This is because the load is not very high, thus the current draw remained the same.

![](https://raw.githubusercontent.com/wendahere/GoGetter/master/Images/withload.JPG)

However, for power calculation, we have to use Max Load, which is the Rated Value given. This is in case anything unexpected happens, such as sudden reversing, will require the rated value.

#### Changes to the design of prototype

If we want to keep the same concept of the collection point, we cannot have the collection point be part of the body. It has to be part of the main door instead. This way, we can still have the linkages connecting the outer and inner flaps, and the main door still can be opened. 

**Changes to Main door cum collection point**

<img src="https://raw.githubusercontent.com/wendahere/GoGetter/master/Images/Door%20wireframe.png" alt="Door wireframe" width="49.5%"> <img src="https://raw.githubusercontent.com/wendahere/GoGetter/master/Images/D%20N.png" alt="D N" width="49.5%">
As we can see from above, a collection area is added to the back of the door, and there are hole cutouts for attaching the hinges. 

<img src="https://raw.githubusercontent.com/wendahere/GoGetter/master/Images/L%20N.png" alt="L N" width="49.5%"> <img src="https://raw.githubusercontent.com/wendahere/GoGetter/master/Images/Flap%20assembly.png" alt="Flap assembly" width="49.5%">
The design of the four bar linkage was also changed to accomodate for the collection point design change *(left)*. The linkages were then assembled along with the the inner and outer flaps in inventor to verify whether the design worked *(right)*

<img src="https://raw.githubusercontent.com/wendahere/GoGetter/master/Images/CP%20N.png" alt="CP N" width="49.5%"> <img src="https://raw.githubusercontent.com/wendahere/GoGetter/master/Images/CP%20New.png" alt="CP New" width="49.5%">
This is how it looks like when the flap assembly is assembled with the main door in CAD.

![MD with B](https://raw.githubusercontent.com/wendahere/GoGetter/master/Images/MD%20with%20B.png)

Fully assembled main door attached to the body in CAD.

**Changes to IO door**

Seeing how plain the original design of the IO door is, Allen made some changes to it. 

<img src="https://raw.githubusercontent.com/wendahere/GoGetter/master/Images/IO%20door%20N%20.png" alt="IO door N" width=""> <img src="https://raw.githubusercontent.com/wendahere/GoGetter/master/Images/IO%20door%20N%20_b.png" alt="" width="">

There are four major changes to the design of the IO door. *From top to bottom,* firstly, a holder is made to slot in Wen Da's phone where we will be using as the screen. Secondly, the cut out for the NFC reader is made into a smaller size as for the prototype we wouldn't be adding that component in. Thirdly, a small hole is also added for us to add in a 5mm LED bulb. Fourthly, another holder for the keypad is also made so that we can slot in the keypad  and it will stay there securely.

Display Screen:

<img src="https://raw.githubusercontent.com/wendahere/GoGetter/master/Images/Phone%20slot%20W.png" alt="Phone slot W" width="49.5%"> <img src="https://raw.githubusercontent.com/wendahere/GoGetter/master/Images/Phone%20slot.png" alt="Phone slot" width="49.5%">
Here shows how Wen Da's phone, an iPhone X will be slotted into the holder.

NFC reader & LED:

![NFC](https://raw.githubusercontent.com/wendahere/GoGetter/master/Images/NFC.png) 

The cutout will be cover by a sheet of transparency, and there will be a holder such that students can leave their card in that holder instead of holding their cards on it for the entire duration when they are redeeming the points for the prizes. The LED below will switch between red and green, where red means "do not remove card", and green neans "you can remove your card".

Keypad:

Instead of using conventional keypads that most vending machine uses. We wanted to use a keypad that has mechanical key switches. Using such key switches elevates the user experience for students, when they press on the switches, it will provide a tactile feedback, this feeling is very different from conventional keypads.

![Numpad case](https://raw.githubusercontent.com/wendahere/GoGetter/master/Images/Numpad%20Case.png)

Reynard designed the holder for the switches, whereas the material used for the holder is acrylic.

<img src="https://raw.githubusercontent.com/wendahere/GoGetter/master/Images/keypad%20assembly%203D.png" alt="keypad assembly 3D" width="62%"> <img src="https://raw.githubusercontent.com/wendahere/GoGetter/master/Images/keypad%20assembly%20S.png" alt="keypad assembly S">

This is how the keypad looks when the keycaps and switches are assembled onto the holder. 

<img src="https://raw.githubusercontent.com/wendahere/GoGetter/master/Images/Numpad.png" alt="Numpad" width="49.5%"> <img src="https://raw.githubusercontent.com/wendahere/GoGetter/master/Images/Numpad%20W.png" alt="Numpad W" width="49.5%">  
Here shows how the assembled keypad is installed onto the IO door.

![IO door assembly](https://raw.githubusercontent.com/wendahere/GoGetter/master/Images/IO%20door%20assembly.png)

Fully assembled IO door attached to the body in CAD.

<img src="https://raw.githubusercontent.com/wendahere/GoGetter/master/Images/3D%20CAD%20F.png" alt="3D CAD" width="49.5%"> <img src="https://raw.githubusercontent.com/wendahere/GoGetter/master/Images/CAD%20F.png" alt="CAD F" width="49.5%">
![3D CAD Open](https://raw.githubusercontent.com/wendahere/GoGetter/master/Images/3D%20CAD%20Open.png)

Here are the final screenshots of the whole CAD assembly in Inventor. 

#### Final assembly of prototype

With the changes made, Allen and Reynard cut the new designs on double and single ply cardboards. Reynard also cut out the acrylic for the keypad.

Main door and IO door: 

![N door](https://raw.githubusercontent.com/wendahere/GoGetter/master/Images/N%20door.JPG)

<img src="https://raw.githubusercontent.com/wendahere/GoGetter/master/Images/N%20PH.JPG" alt="N PH" width="49.5%">
<img src="https://raw.githubusercontent.com/wendahere/GoGetter/master/Images/N%20PH%20A.JPG" alt="N PH A" width="49.5%">
The cardboard for the phone holder is laser cut *(left)* and assembled *(right)*.

<img src="https://raw.githubusercontent.com/wendahere/GoGetter/master/Images/Phone.jpg" alt="Phone" height="845">

This is how it looks with Wen Da's phone when inserted to the IO door. 

<img src="https://raw.githubusercontent.com/wendahere/GoGetter/master/Images/N%20KH.JPG" alt="N KH" width="49.5%"> <img src="https://raw.githubusercontent.com/wendahere/GoGetter/master/Images/N%20KH%20A.JPG" alt="N KH A" width="49.5%">
The cardboard for the keypad holder is laser cut *(left)* and assembeld *(right)*.

<img src="https://raw.githubusercontent.com/wendahere/GoGetter/master/Images/Keypad%20acrylic.jpg" alt="Keypad acrylic" width="49.5%"> <img src="https://raw.githubusercontent.com/wendahere/GoGetter/master/Images/Keypad%20assembly.jpg" alt="Keypad assembly" width="49.5%"> 
The acrylic for the key switches is cut *(left)* and the key caps are assembled onto the key switches which are then assembled onto the acrylic holder. 

<img src="https://raw.githubusercontent.com/wendahere/GoGetter/master/Images/Suspad.jpg" alt="Suspad" height="845">

This is how it looks with the keypad when inserted to the IO door.

<img src="https://raw.githubusercontent.com/wendahere/GoGetter/master/Images/IO%20door%20AF.JPG" alt="IO door AF" width="49.5%">  <img src="https://raw.githubusercontent.com/wendahere/GoGetter/master/Images/IO%20door%20AB.JPG" alt="IO door AB" width="49.5%"> 
*Front view (left), Back view (right)* Finished assembled IO door, with 5mm LED bulb inserted.

<img src="https://raw.githubusercontent.com/wendahere/GoGetter/master/Images/N%20CP.JPG" alt="N CP" width="49.5%"> <img src="https://raw.githubusercontent.com/wendahere/GoGetter/master/Images/N%20CP%20A.JPG" alt="N CP A"width="49.5%"> 
The cardboard for the collection point is cut *(left)* and assembled *(right)*.

![N CF](https://raw.githubusercontent.com/wendahere/GoGetter/master/Images/N%20CPF.jpg)
The cardboard for the inner *(blue)* and outer *(yellow)* flaps are cut out.

![N CPL](https://raw.githubusercontent.com/wendahere/GoGetter/master/Images/N%20CPL.JPG)
The new linkages are printed and assembled as follows.

![N FL A](https://raw.githubusercontent.com/wendahere/GoGetter/master/Images/N%20FL%20A.JPG)
The inner and outer flaps are assembled onto the linkages. 

When we wanted to assemble both the collection point and flaps to the main door, we realised that it is not a good idea to permanently glue the collection point to the main door, in case we need to make any changes or repairs to our prototype.

<img src="https://raw.githubusercontent.com/wendahere/GoGetter/master/Images/N%20CP%20M.JPG" alt="N CP M" width="49.5%"> <img src="https://raw.githubusercontent.com/wendahere/GoGetter/master/Images/N%20CP%20MG.JPG" alt="N CP MG" width="49.5%">
So we came up with a design which consists of a square with a hole in the centre to allow us to join the collection point to the main door using only screws and nuts. The squares with holes are cut out *(left)* and glued together *(right)*. 

![N CP A F](https://raw.githubusercontent.com/wendahere/GoGetter/master/Images/N%20CP%20A%20F.JPG)
The squares are then glued to the the collection point.

![N FL MD A](https://raw.githubusercontent.com/wendahere/GoGetter/master/Images/N%20FL%20MD%20A.JPG)
A hinge is installed onto the collection point then the inner flap is connected to that hinge.

![N MD F](https://raw.githubusercontent.com/wendahere/GoGetter/master/Images/N%20MD%20F.JPG)
For the main door, four holes are created *(as shown by red arrows)* to guide the screws that will connect the collection point with the main door.

<img src="https://raw.githubusercontent.com/wendahere/GoGetter/master/Images/N%20CPMD%20F%20A1.JPG" alt="N CPMD F A1" width="49.5%"> <img src="https://raw.githubusercontent.com/wendahere/GoGetter/master/Images/N%20CPMD%20F%20A2.JPG" alt="N CPMD F A2" width="49.5%">
The collection point is assembled to the main door as shown. 

![N FA C](https://raw.githubusercontent.com/wendahere/GoGetter/master/Images/N%20FA%20C.JPG)
The finished main door and IO door is assembled to the body.

### Friday 9/10/2020

We had a reply for the sponsorship email from a company called ShiokPizza.

####09/10/2020 - Team meeting 7 (10:00am)`
We met up with Mr Soh to go through our prototype.

Use lead screws from misumi, more course, more expensive but larger gaps.

Changed from controller PLC to Pi.

Don’t have to show 3D CAD model, show prototype as we have done it. 

Can claim money if any used for prototype. 

Can be more hardy string such as nylon. Plastic string, fishing line can consider. String must be robust. How they attach the prize must think through, everything must be fuss free. 

Limitation in how much prizes GOS can hang.

Have to prescribe where they can hang the prizes. Have drop sensor to make prize dispenser more foolproof. Can use proximity sensor. 

**Going through function by function:**
Have to change function names.
 
##### Points ID:

Prototype don’t have. Mr Soh likes the idea of RFID slot for students to locate where to put the card. 

LED will change color after points deducted.

*Input Function: 

Keypad, Prize is labeled. 

Press which prize desired. What happens when anyhow type? 

Must have some logic, enter and backspace.

##### Prize Dispensing function: 

Stepper drive lead screw. 

Good to have support (bearing). Have to see real size if it works. 

Lead screw is heavy.

Maintenance, have to remove coupling, have to consider.

##### Storage function: 

Use drawer to pull out to restock. Intend to have 3 tiers for 3 tiers of prizes. Should fix it for them, number of tiers.

Must have features to make it easy to pull out.

Wheel and rail is good, standard part is good. 

Must be limit on how far drawer can be pulled, must put a stopper. 

May consider straighten steel, weld to make drawer. Allen’s labeling as pull out is good as it is highly integrated. 

Must have good housing for all the wires, as there will be many wires. Try to be neat for maintenance. Try to be like Steve Jobs, even if can’t see, have to be neat.

##### Prize Collection: 

Using 3 Bar linkage (Considered 4 bar linkage concept). 

Collection have to be with the door. 

It is good as it is highly integrated. Drop sensor can put on the wall, does not have to be on the door. 

Depending on what material we choose, the door will cost quite a lot of money. 
Prize collection will have funnel to ensure accurate dropping into collection.

##### Coin dispensing: 

Bag prize with coin is good.

Sensory feedback: Can put speakers, low cost. 

Reminder to do BOM. Listen to stakeholder first before doing the BOM and standard parts.

##### Security: 

Have T handle lock.
Can use bigger hinges. If got budget, can buy aluminium profile hindge to buy as standard accessories. Can go to machine design center (AMC) see their industrial hinges. 
Possible to use door hindge.


##### Extra:

Cantilever design, might be too heavy. Consider them by using string, can have many types of prizes, shapes etc.

Sheet metal bending might be expensive depending on design. Better to be flat. Everytime metal is bending, it will stiffen. 

Glass cover will use either poly-carbonate or plexiglass. 

If sheet metal is flimsy, can do welding along the breath side. 

Thickness of sheet metal not considered yet. Steel hollow tube along the frame welded. Make frame out of hollow tube (eg. table legs) don’t have to use sheet metal. Have quarter inch of hollow tube is enough. 

If don’t mind having nut sticking out, can use acorn nut or rivets. 

If got money, can everything use aluminum.

Can put flagging, to tell computer if a row is depleting. 

##### Sponsor: 

Break down of expenses. Write down now much money we request. Then remaining money we will consult the sponsors on what to do.

##### For presentation: 

Let them see the actual moving, see the drop of the prize. 

Most important to show the functions. 

Have more drawers to show array of 3 by 3. 

Like idea of making keypad written GOS. Prototype don’t need cover on top.

Don’t need powerpoint slides, show and tell is enough. If some concepts cannot show, presentation slides can show. 

We let GOS confirm functions first, fabrication let supplier quote. Possible to bend metal to not have hollow tube but still will be flimsy, prefer to have supports. 

#### Sponsorship 

Wen Da talked to ShiokPizza. They are willing to support us as they have supported SP Business School in the past. They are very open to let us visit and learn. We are planning to visit their premises and learn from their machines. Getting money will be secondary. They asked if we are building from scratch or building from a current model. As we are doing as a FYP, we are building the vending machine from scratch.

#### Progress

Wen Da and Reynard finished up soldering the Voltage Regulator. As the specified capacitor was not available, we decided to use higher capacitance.

![voltageregu](https://raw.githubusercontent.com/wendahere/GoGetter/master/Images/12vto5vwithcap.JPG)

We tested the Voltage Regulator and it is working as intended. The 12v supply will be regulated to 5v for the controller.

![test](https://raw.githubusercontent.com/wendahere/GoGetter/master/Images/7805test.JPG)

## Week 5 (11/10/2020 to 17/10/2020) 

## Summary

Finishing touches on the prototype and installing electrical component into the prototype to present to Grace Orchard School. Met with GOS and sponsor, ShiokPizza this week. Arranged to visit ShiokPizza premises Week 6.

### Monday 12/10/2020

During the weekends, Wen Da learned how to use EAGLE. Wen Da talked to the sponsor, ShiokPizza and they will be coming on Friday 3pm to take a look at the prototype.

Wen Da did EAGLE schematics for the voltage regulator. 

![](https://raw.githubusercontent.com/wendahere/GoGetter/master/Images/voltageregulator.JPG)

Wen Da wired the stepper motor driver to test the circuit before making the stripboard circuit. However, he plug 12v into 5v. The motor driver burnt and became usable. This is a learning lesson to double check all the wirings before putting power in.

This is the site used for nema 17 guide. [https://www.makerguides.com/28byj-48-stepper-motor-arduino-tutorial/](https://www.makerguides.com/28byj-48-stepper-motor-arduino-tutorial/)

We used a stepper motor driver uln2003 to try. The 5v stepper motor for it works with the code but when changed to the nema 17 motor 12v, it did not work. The driver might not be able power the 12v stepper motor. 

This is the guide used for uln2003 stepper driver.
[https://www.makerguides.com/28byj-48-stepper-motor-arduino-tutorial/](https://www.makerguides.com/28byj-48-stepper-motor-arduino-tutorial/)

### Tuesday 13/10/2020

####Prototype prep to present to Grace Orchard School.

Allen focused on finishing up the prototype by adding the transparent component and doing finishing touches.

**Final touchup of prototype**

<img src="https://raw.githubusercontent.com/wendahere/GoGetter/master/Images/MD%20T.jpg" alt="MD T" height="800">

A sheet of transparency is used to cover up the huge rectangular cut out of the main door.

<img src="https://raw.githubusercontent.com/wendahere/GoGetter/master/Images/Card%20holder%20F.jpg" alt="Card holder F" height="800"> <img src="https://raw.githubusercontent.com/wendahere/GoGetter/master/Images/Card%20holder%20B.jpg" alt="Card holder B" height="800">

A card holder for the NFC cut out was made from folding the outermost layer of cardboard. It is folded and glued onto the cutout for NFC card reader in the IO door. *Front view (left), back view (right)* 

<img src="https://raw.githubusercontent.com/wendahere/GoGetter/master/Images/IO%20T.jpg" alt="IO T" height="800">

A small sheet of transparency is cut out and then glued onto the cutout for NFC reader in the IO door.

![Test NFC](https://raw.githubusercontent.com/wendahere/GoGetter/master/Images/Test%20NFC.jpg)
Here is a sample of how the holder works. Students can choose to either physically hold their card onto the reader until the LED below flashes green or leave their card in the holder when they redeem their prizes.

For this prototype we did not implement any physical locking mechanism but we wanted to show GOS what kind of security system they would expect from this machine. So we went to take a picture of the type of lock we wanted to use from an existing vending machine in school, then printed a sticker of it and applied it on the IO door.

<img src="https://raw.githubusercontent.com/wendahere/GoGetter/master/Images/reference.jpg" alt="reference" width="49.5%"> <img src="https://raw.githubusercontent.com/wendahere/GoGetter/master/Images/sticker.jpg" alt="sticker" width="49.5%">
This vending machine here *(left)* has the type of T-handle security lock we needed. Here *(right*) is the image of our prototype with the sticker *(green arrow)* of the same lock applied on it.  

![handle](https://raw.githubusercontent.com/wendahere/GoGetter/master/Images/F%20H.jpg)
Reynard also added a handle to the outer flap on the main door, so that it is easier for users to test out our prototype during our next client meeting.

To ensure the doors of the prototype stays shut at all times, we used magnets to achieve this. On top of that, we also wanted to show that in the event the machine requires any form of maintainance, the IO door has to be opened first before the main door can be opened.

<img src="https://raw.githubusercontent.com/wendahere/GoGetter/master/Images/magnet.jpg" alt="magnet" height="800">

Four magnets are installed onto the prototype in the four points as shown *(green circles)*. 

<img src="https://raw.githubusercontent.com/wendahere/GoGetter/master/Images/paper.jpg" alt="paper" height="800">

To emulate that the IO door has to be opened first before the main door, pieces of paper are added to the main door as shown *(red arrows)*. This acts like the actual recessed layer of the main door that we would implement in the actual vending machine to ensure that the main door only opens after the IO door opens.

<img src="https://raw.githubusercontent.com/wendahere/GoGetter/master/Images/hole.jpg" alt="hole" height="800">

As we would be running a stepper motor to demonstrate our dispensing mechanism, we needed some form of cable management. A hole is cut out at the back of the prototype so that our circuit and microcontroller can be hidden away at the back of the prototype when everything is connected.

**Stepper motor**

Reynard brought more A4988 stepper motor drivers. Wen Da wired A4988 circuit.

![a4988 circuit](https://raw.githubusercontent.com/wendahere/GoGetter/master/Images/a4988circuit.JPG)

Testing on the breadboard, the stepper motor spun well for awhile. However, the stepper motor started to stutter-step. This meant there might have been a problem with the stepper motor. However, after checking the circuit, Wen Da realised that he put the wrong transistor. He put 47uF instead of 100uF. In theory, putting higher capacitance is better. 

In this case, the capacitor acts as a spare battery, having low capacitance, there is not enough voltage from the capacitor to sent to the motor, resulting in the motor jittering.

Wen Da wired the stripboard and Reynard soldered the wires, A4988 driver and pins on the stripboard.

<img src="https://raw.githubusercontent.com/wendahere/GoGetter/master/Images/a4988stripboard.JPG" alt="a4988back" width="49%"> <img src="https://raw.githubusercontent.com/wendahere/GoGetter/master/Images/a4988back.JPG" alt="a4988soldered" width="49%">

After testing the stripboard, the stepper motor moves smoothly with the 1000uF capacitor, due to having much higher capacitance, the stepper motor does not jitter step or have much trouble. The dispensing function was ready to be presented.

This is the code used for testing:

	const int stepPin = 3; 
	const int dirPin = 4; 
 
	void setup() {
	  // Sets the two pins as Outputs
	  pinMode(stepPin,OUTPUT); 
	  pinMode(dirPin,OUTPUT);
	}
	void loop() {
	  digitalWrite(dirPin,HIGH); // Enables the motor to move in a particular direction
	  // Makes 200 pulses for making one full cycle rotation
 	 for(int x = 0; x < 200; x++) {
 	   digitalWrite(stepPin,HIGH); 
 	   delayMicroseconds(500); 
	    digitalWrite(stepPin,LOW); 
	    delayMicroseconds(500); 
	  }
	  delay(1000); // One second delay
  
 	 digitalWrite(dirPin,LOW); //Changes the rotations direction
	  // Makes 400 pulses for making two full cycle rotation
	  for(int x = 0; x < 400; x++) {
 	   digitalWrite(stepPin,HIGH);
	    delayMicroseconds(500);
 	   digitalWrite(stepPin,LOW);
  	  delayMicroseconds(500);
 	 }
 	 delay(1000);
	}


### Wednesday 14/10/2020

Allen worked on the Journal and did some additions on the prototype. We did another test and took a video of it.

#### How to load prizes

**Method**

Nylon

Weaved nylon

Sewing thread

#### Finished protoype

## Show pics

Wen Da received feedback on his 7805 Voltage Regulator Schematic, the voltage input was supposed to be 12v, not 24v and should rotate the capacitors to make it less confusing. Only 1 ground is needed and do not need + or - at input and output. The filtering of voltage is called Low-Pass filter.

![](https://raw.githubusercontent.com/wendahere/GoGetter/master/Images/voltageregulatorv2.JPG)

Wen Da did the EAGLE circuit drawing for A4988 circuit with Arduino. There was some trouble as the library did not have A4988 and stepper motor. After installing the libraries, everything worked well.

![](https://raw.githubusercontent.com/wendahere/GoGetter/master/Images/a4988%20with%20arduino.JPG)


Wen Da designed a keychain for ShiokPizza the sponsor. Allen and Wen Da laser cutted it. This was made as a token of appreciation for our sponsor and to ensure that the sponsorship will go well.

![](https://raw.githubusercontent.com/wendahere/GoGetter/master/Images/sponsortoken.JPG)

### Thursday 15/10/2020

We did presentation slides

insert link [here]().

Allen did a video (for prototype)

embed vid here [here]()

### Friday 16/10/2020

We had a meeting with GOS 10am and another meeting with ShiokPizza 3pm.

Meeting with GOS 10am:

Questions to ask GOS - 

1. How user friendly the vending machine is for the staff to operate and for the students to interact?
2. Do they like the design?
3. Ask them individually about each function
4. What are some of the pain points that a staff or student may experience?
5. Layout of the IO interface
6. What other additions to the machine do they want?
7. Are the compromises acceptable? (needing them to prepare the prizes beforehand)
8. Is using a phone to give points acceptable?
9. How many points does a student earn per day {this affects how often a staff needs to give points to the student) 
10. Each level what are the different number of types of prizes (the min number)
11. Do they want us to implement special prizes (principal prize)
12. Average height of the student body?
13. For the layout of the storage and IO interface

Remarks 


- Plug in that our budget increased by abit, but should be able to make it full sized, however certain functions may have to have some corners cut

What we did:


- Gave a short demo on how teachers would give students points
- Showcased prototype with each working function

**Bolded: Important to take note**
*Italic: Action required*

GOS asked: 



- What is the prevention method for 2 prizes dropping?


- How many types of prizes per row? 


- How often do they need to replenish? (they see the prototype quite small)
	- Afternoon session over 100 students that redeems prizes


- Size of actual machine? Estimate how many prizes we can put


- How many motors per row? And can give more than 3-4? To ensure a variety of prizes.
	- They want about 5 stepper motors per level
	- For the current system, all 3 tiers have about the same number of prizes


- Shift Stepper motor left and right to edit space required due to prizes. (what we can do)


- Maintainability: eg motor spoil and lead screw spoil then how? 
	- We use standard parts so easy to buy and specially made parts will give extra as spares (what we said)* 


- Will they (student) know which prizes need to press what button?
	- Color code, A row is yellow etc
- **Students might find trouble with A1, doing something like Yellow 1 is better.**


- Smart TV can do? 
	- Smart TV has no NFC function.
	- If a student has 100 points and wants to redeem 2-50points items instead of 1-100 point items. 
		- Is OK (what we said)

- Recording: Is there a way to capture data, which prizes not “selling” etc? 
	- **Record down name and points redeemed. Name, Class and no. points redeemed**
		- Current method: excel sheet manually input number of points, so can see from jan to feb how many points
		- Teacher will check who have not redeemed their points and will find out why etc..

- Dropped card concern
	- Have ID on the card so cant use other people card
	- **Have name on the card to identify is enough (Conclusion by GOS)**
	- Current system: if student lost their card, if anyone find their card and give to teacher then they will return to that student, else teacher will give another card


- *Can have separate devices to input points* 
	- Separate readers installed in class
	- Can connect a laptop to the reader to give points. Usually teachers give points in class
	- However, teachers also give out points outside of the classroom as well. Look into NFC readers that can read and write. Can put in a common corridor
	- Teachers have school issued laptops, able to control what software can be installed. 


- *Regarding budget:* 
	- They asked if possible for GOS to add on money for more columns and rows 
	- GOS won a prize and will donate money when necessary




- Want to see the screen display, how many points, press keys for prizes, please make your selection etc. **Messages are important**
	- **Let them know what we made so they can give feedback, so they can help us with the needs of the students (GOS said)**






- Layout of the machine: 
	- Younger students are the main issue as they are shorter. Keypad can be installed lower. Screen cannot be too low. 
	- Mr Soh will give ergonomic data so we can take average. 
	- Can make steps/stool for shorter students to use the machine. They currently use it so it's fine to use it. 
	- **Don't need to implement the design.**


- **Need to put a cardholder as a pressing button while holding the card is not easy for the student**



- Regarding forgetting card on the machine
	- *Install audio/visual* 
	- *Please take your card*


- Bolting down the machine, have to check if possible but if its an safety issue then will allow.
	- **Check if machine needs to be bolted down for safety**



- *Glass*
	- Don’t want something that will break from punch. 
	- If it breaks, it won't break into pieces.



- Packaging is low cost, it is okay with them to pack the prizes



- *Special prizes and adhoc prizes can be done offline because few students redeem it*



- Not worried about lead screw bending



- Extra:
	- Make laser cut tokens for GOS.
	- Only android phones can give points: FA Watch will always tap to check how much money is inside, many students want to tap just for fun.

*Pain Point*: 
Teachers sometimes anyhow chop, put +3 or +2, making it hard to count the number of points.

**Students might not understand how point systems work, hard for students to tell which number is bigger, 50 or 100 etc**.


- Light up which row can be chosen will be useful
- Make a meter to reflect how much points currently have, 0 to 100 in a bar (in display)
- Have LED strip to show how much points

**Next meeting with GOS: Show CAD files and make video/animation.**

## Meeting with ShiokPizza 3pm:


They have have old machines and able to edit it.

Don't mind working together but want to know how can they help.

Hanging type vending cause more jam compared to coil type.

Can take entire old vending machine for parts

Can arrange to bring over to SP with no charge

Normally these type vending machine are shipped from china

Factory in amk

Can consult their engineers for help

Thurs most likely but will get back to us

Can have a bracelet with a chip for payment.


### What to do for weekend:

Allen: setup report template, look into metal design bending for CAD, what kind of metals we can use, look into hollow tubes. 

Wen Da: finish up on journal and report, learn Pi, circuit stuff

Reynard: programming ( look into NFC)


## Week 6 (18/10/2020 to 24/10/2020) 

## Summary

We visited sponsor's warehouse and were given one working vending machine to be transported the next week. After learning that industry standard is DC motors in vending machine and we were sponsored the 24v DC motors as well, we decided to switch to DC motors. We further worked on refining the design after looking at the insides of a vending machine. We also made a PCB using chemical etching. 

### Monday 19/10/2020

Wen Da worked on RaspberryPi. 

Steps to follow:

1. Format the SD Card
2. Follow this link [https://www.raspberrypi.org/downloads/](https://www.raspberrypi.org/downloads/) , download the Raspberry Pi Imager for Windows and select the recommended OS, select the correct SD Card (important)
3. Let the program run, it will take a while
4. Eject the SD Card and plug into the Pi
5. Plug in mouse, keyboard and HDMI cable before plugging in the power

Initially, there was a problem with the monitor, the monitor kept a fuzzy static image.

![fuzzy](https://raw.githubusercontent.com/wendahere/GoGetter/master/Raspberry/Images/fuzzyscreen.JPG)

After trying on a larger resolution monitor, the same Pi with same SD Card worked. This meant that there was a problem with the resolution. After reading this site:
[https://pimylifeup.com/raspberry-pi-screen-resolution/#:~:text=With%20the%20tool%20loaded%20on,set%20for%20this%20current%20display.](https://pimylifeup.com/raspberry-pi-screen-resolution/#:~:text=With%20the%20tool%20loaded%20on,set%20for%20this%20current%20display.)

We learned that the resolution can be changed in the config text file. We changed the hdmi_group to "hdmi_group=2" and it worked well.

![](https://raw.githubusercontent.com/wendahere/GoGetter/master/Raspberry/Images/catgif.JPG)

Next we ensured that the Pi was updated. 
Steps to update:
1. Connect Pi to internet
2. Open Terminal in the Pi
3. Type "sudo apt-get update && sudo apt-get upgrade
4. Let the program update
5. Press y and enter when prompted to use up disk space
6. Done!

It should look like this

![](https://raw.githubusercontent.com/wendahere/GoGetter/master/Raspberry/Images/update.JPG)

Next Wen Da setup remote control for the Pi. This makes it easier to control the Pi as a monitor is not required. For this, we will be using VNC Server. We followed this guide [https://www.raspberrypi.org/documentation/remote-access/vnc/README.md](https://www.raspberrypi.org/documentation/remote-access/vnc/README.md)

Steps to install VNC:

1. Create a account
2. Watch the video to enable Home subscription (Free for 5 users)
3. In Pi Terminal, type "sudo apt update" and "sudo apt install realvnc-vnc-server realvnc-vnc-viewer"
4. Enable VNC in Pi
5. Select Menu > Preferences > Raspberry Pi Configuration > Interfaces
6. Ensure VNC is Enabled
7. Download VNC Viewer on your PC that is controlling the Pi
8. Login on your PC and Pi 
9. From your computer, click on the Pi and connect
10. For login details, username: pi, password:raspberry
11. Done!


![](https://raw.githubusercontent.com/wendahere/GoGetter/master/Raspberry/Images/VNC.JPG)

Allen sourced for materials. (lead screws)


### Tuesday 20/10/2020

Wen Da continued with RaspberryPi. He did a simple blinky program to learn about the GPIO. This guide was followed:
[https://raspberrypihq.com/making-a-led-blink-using-the-raspberry-pi-and-python/](https://raspberrypihq.com/making-a-led-blink-using-the-raspberry-pi-and-python/)

This is the code used:

	import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library
	from time import sleep # Import the sleep function from the time module
	GPIO.setwarnings(False) # Ignore warning for now
	GPIO.setmode(GPIO.BOARD) # Use physical pin numbering
	GPIO.setup(8, GPIO.OUT, initial=GPIO.LOW) # Set pin 8 to be an output pin and set initial value to low (off)
	while True: # Run forever
	 GPIO.output(8, GPIO.HIGH) # Turn on
	 sleep(1) # Sleep for 1 second
	 GPIO.output(8, GPIO.LOW) # Turn off
	 sleep(1) # Sleep for 1 second

From this, we learned that there are 2 different types of pin numbering. Physical Pin number is to use the number labeled on the pins as the GPIO pin numbering rather than the number attached to the pin (eg. GPIO_14).

If this line is used: 	GPIO.setmode(GPIO.BOARD) # Use physical pin numbering, then the Pi will be using the number in the circle as the GPIO numbering, else using GPIO.setmode(GPIO.BCM), will use the GPIO_numbering instead (Broadcom SOC Channel).


![](https://raw.githubusercontent.com/wendahere/GoGetter/master/Raspberry/Images/pinout.JPG)


Afterwards, we setup the Stepper Motor circuit on the Pi. We followed this video. 

[https://www.youtube.com/watch?v=LUbhPKBL_IU&t=771s](https://www.youtube.com/watch?v=LUbhPKBL_IU&t=771s)

![](https://raw.githubusercontent.com/wendahere/GoGetter/master/Raspberry/Images/IMG_5118.JPG)

After turning of the Pi, the stepper started to move, this meant that we have to setup a fail open circuit.

Wen Da drew out the circuit for DPDT Relay with Raspberry Pi and A4988 Driver

![](https://raw.githubusercontent.com/wendahere/GoGetter/master/Raspberry/Images/DPDT.JPG)

Allen continued to source for materials and did ergonomics study on the anthropometric data of **insert nationality/race** to determine the best layout for our components.

**insert data**

**insert allen testing on his brother**


### Wednesday 21/10/2020

Allen made a mockup for the layout of the vending machine 

**insert pictures**

Wen Da did drawing of PCB and etching to make the PCB. 

![](https://raw.githubusercontent.com/wendahere/GoGetter/master/Electrical%20Component/pcbv1.png)

We decided to make the PCB using etching.

First step is to print the PCB on a special paper. The white portion will be etched away.
![](https://raw.githubusercontent.com/wendahere/GoGetter/master/Electrical%20Component/PCB%20Etching/Electrical%20PCB/IMG_5125.JPG)

AFterwards, cut and stick the paper on a stripboard with thin layer of copper.

![](https://raw.githubusercontent.com/wendahere/GoGetter/master/Electrical%20Component/PCB%20Etching/Electrical%20PCB/IMG_5126.JPG)

Use a kapton tape that is heat resistant and can stick at high temperatures.

![](https://raw.githubusercontent.com/wendahere/GoGetter/master/Electrical%20Component/PCB%20Etching/Electrical%20PCB/IMG_5127.JPG)

Put a layer of foam and baking paper to protect the special paper from smudging. Set the temperature of the heat press to 170 degrees Celsius. 

![](https://raw.githubusercontent.com/wendahere/GoGetter/master/Electrical%20Component/PCB%20Etching/Electrical%20PCB/IMG_5129.JPG)

![](https://github.com/wendahere/GoGetter/blob/master/Electrical%20Component/PCB%20Etching/Electrical%20PCB/IMG_5130.JPG)

![](https://raw.githubusercontent.com/wendahere/GoGetter/master/Electrical%20Component/PCB%20Etching/Electrical%20PCB/IMG_5131.JPG)

Close the press and wait for 40 seconds. 

Peel off the paper and the black portion should remain on the copper portions.
![](https://raw.githubusercontent.com/wendahere/GoGetter/master/Electrical%20Component/PCB%20Etching/Electrical%20PCB/IMG_5136.JPG)

As etching will remove copper portions, we cut away the perimeters of the copper that is unused.

Mix 1:1 portion of 3% Hydrogen Peroxide and Vinegar. If the hydrogen peroxide is 6%, mix a 2:1 with 2 being Vinegar. Add half a teaspoon of salt, it does not have to be accurate, but too much salt will cause too much bubbles when copper is being rubbed off.

![](https://raw.githubusercontent.com/wendahere/GoGetter/master/Electrical%20Component/PCB%20Etching/Electrical%20PCB/IMG_5137.JPG)

Put the copper PCB in the chemical bath and irritate the liquid to remove the etching from the copper board.

![](https://raw.githubusercontent.com/wendahere/GoGetter/master/Electrical%20Component/PCB%20Etching/Electrical%20PCB/IMG_5139.JPG)

After testing for continuity to check if the board is working, using Aerosol to remove the white portions of the PCB.

![](https://raw.githubusercontent.com/wendahere/GoGetter/master/Electrical%20Component/PCB%20Etching/Electrical%20PCB/IMG_5141.JPG)

End Product.

![](https://raw.githubusercontent.com/wendahere/GoGetter/master/Electrical%20Component/PCB%20Etching/Electrical%20PCB/IMG_5143.JPG)

This also works for copper tape:

![](https://github.com/wendahere/GoGetter/blob/master/Electrical%20Component/PCB%20Etching/Electrical%20PCB/IMG_5144.JPG)

### Thursday 22/10/2020

Reynard and Wen Da worked on Double Pole Double Throw Relay with Stepper motors. We managed to make it work, when the relay was actuated, the stepper motor switched to the other stepper motor.

At 2:50pm, Mr Soh drove us to Techplace 1, where the warehouse of the vending machines were located.

We looked through how the vending machines worked and what motors they used. We would be sponsored one working vending machine.

Allen design the frame so we could send it for quotation.

### Friday 23/10/2020

We decided to change the dispensing mechanism to spring instead of lead screw.

Wen Da tested the Pi with the new motor given. We learned that 2.05 seconds would result in 1 rotation of the motor.

![](https://raw.githubusercontent.com/wendahere/GoGetter/master/Raspberry/Images/IMG_5184.JPG)

We also learned that with only spring, the motor would take 0.05A of current

![](https://raw.githubusercontent.com/wendahere/GoGetter/master/Raspberry/Images/IMG_5186.JPG)

Afterwards, we had our Intro to Entrepreneurship class.

After the class, Allen and Wen Da went to Mr Walter Chan, the Executive in charge of T11c Fablab, to talk about the placement of vending machine. We were allowed to put the vending machine there as long as we work there from then onward. We talked to Mr Edward Tay from W12 workshop about the hollow tube frame. He gave us his opinion and we learned that we might not get what we asked for, eg angle of frame not exactly 90 degrees, length not exact if we do not give the tolerance. 

We also learned that giving too small of tolerance eg +- 0.01mm is too much and +- 0.05 is okay but the product given might not fit what we are planning if both sides are out.

### Weekends 24-25/10/2020

Allen did CAD for the motor gear box given to us by the sponsor, since there isn't any available 3D files of it online. He did torque calculations. Designed the feedtray. 


Wen Da started to learn how to make GUI display. This youtube video guides were followed: [https://www.youtube.com/watch?v=s81_WnM1oJA](https://www.youtube.com/watch?v=s81_WnM1oJA)

Steps:
Install all tools, open console and type and enter the commands:
"sudo apt-get update" 

"sudo apt-get dist-upgrade" 

"sudo apt-get install qt5-default" 

"sudo apt-get install qtcreator" 

"sudo apt-get install libqt5serialport5" 

"sudo qpt-get install libqt5serialport5-dev"
 
"sudo apt-get install qttools5-dev-tools"

"sudo apt-get install eric" (Python Compiler that I will be using)

Restart the Pi and launch Eric



Code used:

	from PyQt5.QtWidgets import QApplication
	from ui.mainWindow import MainWindow

	if __name__=="__main__":
 	   import sys
 	   app=QApplication(sys.argv)
 	   ui=MainWindow()
 	   #ui.showFullScreen()
 	   ui.show()
 	   sys.exit(app.exec_())

## Week 7 (25/10/2020 to 31/10/2020) 
We met up with Singapore Polytechnic Special Needs Education Expert (Sen Center). Wen Da designed and chemical etched a PCB for Motor Matrix Control. Allen worked on the Vending Machine Design. Reynard worked on Keycaps and soldering Keypad Matrix.

At end of the week, we collected a sponsored Vending Machine given from Blue Sky Tree. We took apart the vending machine to study and to use as parts.

### Monday 26/10/2020

Allen continued working on the feedtray design for the vending machine. Since we will not be using the existing feedtrays from the vending machine that was given to us, as it does not serve the purpose we need, which is to hang the prizes on the coil. He also sourced for the different materials that will be used to make the feed tray (angle bar, and sheet metal), and did research on what grade of aluminium or steel is most suitable for us.

Talk about the angle bar

Also modelled a drawer roller slide. 

**insert pictures**

Wen Da tested if using transistor as a switch for power side would work. He was unsure as the typical switch use is to cut off the ground side, not the power side. This was tested on tinkercad.

![](https://raw.githubusercontent.com/wendahere/GoGetter/master/Raspberry/Images/powersidetest.JPG)

Wen Da drew out the matrix wiring control for motors (5 by 3 and 5 by 4) on eagle. He later tested 1 by 1 matrix as he was unsure if the GPIO control common GND would connect to the 2nd transistor (GND Side)

![](https://raw.githubusercontent.com/wendahere/GoGetter/master/Raspberry/Images/transistormatrixtest.JPG)

The LED lights up means the 1 by 1 matrix works. This means that 5 by 4 etc, would all work as well.

### Tuesday 27/10/2020

Allen consulted with Mr Soh on the design of the feedtray. Where Mr Soh mentioned if we were to proceed with sheet metal bending, we needed to include corner reliefs for the bends so as to prevent tearing from happening while bending. He said to send the design for quotation first and to see the prices for 1mm steel and 2mm aluminium.

Allen also 3D printed the coil mount he modelled during the weekends to see whether it fits, and to test whether can we 3D print spare parts for it for GOS should any of it break during operation. 

Reynard did the keypad. He did matrix wiring on the key switches, and programmed an arduino micro for the keypad.

Wen Da carried on PCB Design for Motor Matrix wiring.

**insert pictures**

#### Special needs education (SEN) expert meeting

We had an appointment Ms Nicole Daswani, an expert on special needs education from SP's SEN centre. We wanted to know more about 

### Wednesday 28/10/2020

Wen Da made the PCB board for etching fit the board. The board given was smaller than expected so he made it smaller to fit. However, the container to put the chemical was too small so we decided to continue on Friday due to sponsor meeting on Thursday. Allen and Wen Da laser cut a larger sized container for etching.

Allen made the necessary adjustments to the feed tray design before making the 2D drawing for it. As well as making a 1mm variant of the design if we decide to make the feed tray with steel. Allen also made the 2D drawings for the motor bracket and the handle.

**insert pictures**

Reynard continued to work on the keypad. Ask Louis to flash the arduino micro. Considered making a PCB as the wires leading to the arduino micro is very messy. 

### Thursday 29/10/2020

Allen brought parts from Aircon Lab in SP.

Wen Da tested all of the power supply units Allen brought to ensure that it is working. Wen Da went to Easy M Ltd Pte at Republic Plaza, #06-00 to see what parts he could take for the project.

Allen also made multiple designs of the 

### Friday 30/10/2020

We gathered our comrades to assist us in moving the sponsored vending machine from Techplace 1 in Ang Mo Kio Ave 10 to T11c in Singapore Polytechnic. Reynard stayed behind in Singapore Polytechnic due to his bad knee and there is a shelter to be moved before the Truck can move into T11c. 

Shelter to be moved:

![](https://raw.githubusercontent.com/wendahere/GoGetter/master/Images/Collection/5692770c-e486-4bc8-b8b4-09d3d65d0a59.jpg)

Wen Da liaised with a transport company called LongShot Transport, for a 8-footer lorry with tail lift and one pallet jack.

The driver came very early.

![](https://raw.githubusercontent.com/wendahere/GoGetter/master/Images/Collection/E7F6F8B8-3345-4C1C-AF38-442881FE71B8.jpg)

Allen and our comrades helped move the vending machine to the loading bay. 
![](https://raw.githubusercontent.com/wendahere/GoGetter/master/Images/Collection/c798f85a-eda3-4921-b7b1-ba3ab5f7caa2.jpg)

![](https://raw.githubusercontent.com/wendahere/GoGetter/master/Images/Collection/IMG_5269.JPG)

We are very thankful for the company Blue Sky Tree for sponsoring their vending machine! We parked the vending machine at T11c at the back. This will be our working area from now onwards.

![](https://raw.githubusercontent.com/wendahere/GoGetter/master/Images/Collection/IMG_5273.JPG)

After a short break, Allen and Reynard worked on taking apart the vending machine while Wen Da worked on chemical etching the PCB.

Working on PCB:

![](https://raw.githubusercontent.com/wendahere/GoGetter/master/Images/Collection/IMG_5275.JPG)

![](https://raw.githubusercontent.com/wendahere/GoGetter/master/Images/Collection/IMG_5276.JPG)

The heat press looked promising however....Looking at the top-ish left portion of the board, there is a part that did not did press properly. We tried using a black marker pen to protect the copper, however, after the chemical bath and wiping away with Aerosol, it turns out that marker ink did not protect the copper.

![](https://raw.githubusercontent.com/wendahere/GoGetter/master/Images/Collection/IMG_5281.JPG)

After using Aerosol to wipe away the protection and testing continuity, it turns out that the bad portion did had continuity! It will work fine. Wen Da is planning to drill hole and solder the components on Monday. As the board is large, Wen Da and Allen made a larger size box using Acrylic and waterproofed it using tape and Acrylic Glue. This board required 5 chemical baths of 100ml to etch away the copper.

### Weekends 31/10 - 1/11/2020

Wen Da brought the Power Supply Unit and a row of Motor and it's PCB home to work on it. The PSU had 2 input to power the machine in parallel as only 1 input (wall plug) might not have enough current to power the machine.

![](https://raw.githubusercontent.com/wendahere/GoGetter/master/Images/Collection/IMG_5302.JPG)

The PSU used Molex cables to connect the wires. 

The Mechanical Circuit Breaker is C16, this meant that it was a slow acting 16A MCB. There is 2 inputs and 2 outputs, for live and neutral. This means that it is able to detect if there is deviation due to poor insulation. It is not the best MCB for our purpose, Type A is better as it is fast acting, but it will work fine. The Live and Neutral will be connected to the MCB then to the PSU. 

The Earth will be connected to the casing and parallel connected to the PSU. (PSU required Live, Neutral and Earth) Connecting Earth to the casing is to ensure that anyone who touches the Vending Machine will not be shocked if there are any live loose/open wires touching the casing due to any reason.

![](https://raw.githubusercontent.com/wendahere/GoGetter/master/Images/Collection/IMG_5305.JPG)

The given casing with the PSU also had a temperature controller. It will not be used as it is not required.

![](https://raw.githubusercontent.com/wendahere/GoGetter/master/Images/Collection/IMG_5306.JPG)

This is the Power Supply Unit. 24v, 10A. Out of all of our 24V power supply we had, this is the highest current rating we have. We will be using this Power Supply Unit.

![](https://raw.githubusercontent.com/wendahere/GoGetter/master/Images/Collection/IMG_5308.JPG)

The PCB they used for matrix control was very useful. I learned that the holes to put the molex female component were Vias. This meant that I could connect the top copper and bottom copper to the molex female component and only solder the component at the bottom. I would not need to solder the top copper for the component to connect as there is the Via to connect the bottom to the top copper.

Allen continued to work on the CAD design of the vending machine. He focused on designing the metal sheets that would be used to cover up the hollow tube frame. 

**insert pictures of the different metal sheets for the frame**

The way we will be installing the sheets onto the frame is by blind riveting. Allen learnt that the spacing between each rivets also known as rivet pitch must be at least 3 times the rivet diameter, althought the preferred distance is 3.5 times the rivet diameter. Another thing to note is the edge distance of rivets, it should not be less than 2 times the diameter of the rivets. The recommended edge distance is 2.5 times the rivet diameter, this is so that the rivet holes can be enlarged in the future without violating the miniumum edge distance. It is important that the minimum edge distance is met. This is because, if rivets are placed to near the edge of the sheet, the sheet may crack or pull away from the rivet while under load.

To find out more about the basics of riveting, here are some links: [link 1](https://www.youtube.com/watch?v=FY8Nn7_6Erc&ab_channel=HomebuiltHELP), [link 2](https://www.flight-mechanic.com/structural-fasteners-solid-shank-rivets-installation-of-rivets/), [link 3](https://www.tpub.com/air/13-25.htm).

**show pic of the frame with rivet holes** 

There was a concern with the design if we 

**show pic of the coils being in line, then the prizes might get caught by the coils below**

One method that we came up with is to cut the coils short

**show pic of the solution**

## Week 8 (1/11/2020 to 7/11/2020) 

We took apart the vending machine to reuse their parts. Wen Da finished his chemical etched PCB for motor control.

### Monday 02/11/2020

Allen and Reynard continue to take apart the vending machine to learn its inner workings. While Wen Da worked on his PCB.

Wen Da drilled holes for the components for the PCB matrix motor control. He brought his 0.8mm drill bit and a desk drill press. 

![](https://raw.githubusercontent.com/wendahere/GoGetter/master/Electrical%20Component/PCB%20Etching/Electrical%20PCB/Part2/IMG_5321.JPG)

After checking the other side to see if the holes drilled through, Wen Da found out that the back cracked. This is not good as the component pin cannot go through the hole drilled.

![](https://raw.githubusercontent.com/wendahere/GoGetter/master/Electrical%20Component/PCB%20Etching/Electrical%20PCB/Part2/IMG_5322.JPG)

Wen Da used a thin scrap wood board, about 3mm and put under the PCB to drill through. The back of the PCB had no cracks. Wen Da used a 1mm drill bit to "debur" the cracks.
Wen Da put all the components in the respective locations and taped it in place for soldering.

![](https://raw.githubusercontent.com/wendahere/GoGetter/master/Electrical%20Component/PCB%20Etching/Electrical%20PCB/Part2/IMG_5325.JPG)


Allen met up with Mr Soh to discuss the design of the vending machine.

**Dispensing mechanism:**

- For the design of the feedtray, Mr Soh stated that if the other 3 sides of the wall of the body is not load bearing, then their height need not to match the height of the front wall. This might help to cut cost in the manufacture of the feed tray drawers.
- For the motor bracket, Mr Soh suggested to change the design into using bent 3mm steel,  
- For our angle bar that is used to support the coil, the bending relief should be perpendicular to the bending line rather than parallel to it.
- With regards to the chance a prize on the highest level might get caught by the coils on the level below it when it gets dispensed, Mr Soh suggested to make ramps for the top 2 levels.
- Motor bracket change to use 3mm thick stainless steel (bending), but same design and dimension.

**Frame:**

- The panel thickness is changed from 2mm to 1mm, and we will most likely use either phosphated steel or powder coated mild steel.
- The width of the frame is increased by 150mm and the thickness is increased by 200mm. Hence, the final dimension of our vending machine is: 1150 x 1450 x 800mm
- For the rivet pitch, we would use 20 times the rivet diameter. Don't need to follow the rule of thumb.
- To mount the drawer runners to the frame, it will be mounted on horizontal hollow tubes, that are 1mm thick, where rectangular cut outs are made in the the tubes so that the drawer runner can slide into them and be locked in place. If that doesn't work, the drawer runners will be welded directly onto the frame.
- Talk about making the left panel transparent, use polycarbonate sheet instead of metal sheet, so that students will be able to peer through and see the dispensing mechanism. This allows students to learn about physics (link to what was said by SEN centre expert, allow the students to gain transferable knowledge).

### Tuesday 03/11/2020

Allen laser cut and bent 3mm acrylic to test out the new motor bracket.

**insert pic here**

Allen worked on creating a ramp for the bottom 2 levels of the feed tray. After creating the first design, he realised that the overall design can be simplified. This way there isn't a need to increase the width of the frame and the thickness can be increased by 100mm instead of 200mm. New frame dimension: 1000x700x1450mm. 

**show ramp design 1**

**show ramp design 2** 

Allen also worked on the panels for the collection point at the door.

**show pictures**

Did a layout test, found out that 1450mm might not be a suitable height

**show pictures**

Wen Da got an expert to help him solder the components on Monday evening. 

![](https://raw.githubusercontent.com/wendahere/GoGetter/master/Electrical%20Component/PCB%20Etching/Electrical%20PCB/Part2/54B77140-9261-48C7-8C03-DA31C23B9BD8.jpg)

Wen Da cut the extra pins after checking continuity of the circuit. However, Wen Da realised that the PCB had a mistake, one of the transistor's middle pin was shorted to the side pins. Wen Da consulted few experts and got few opinions on how to fix it. 

The first method was by using wiring wrapping. Using a tool and wire wrap, the copper wire can wrap around a pin, in this case the middle transistor pin and other side solder to the copper required. This method requires less soldering but is not permanent as there is no solder on the wire wrap connecting to the middle transistor pin.

The second method which was used is simply to "jumper" the middle pin of the transistor to the copper required. The middle pin can be bend 90 degrees and cut a bit shorter. A wire will be soldered on it and the other end soldered on copper on the PCB.

![](https://raw.githubusercontent.com/wendahere/GoGetter/master/Electrical%20Component/PCB%20Etching/Electrical%20PCB/Part2/IMG_5340.JPG)

After a quick continuity check to check if there are any shorts, Wen Da went and test the board with motors.

Wen Da tested his circuit and found problems. The motor control did not work. After testing the low-side transistor switch, he found out that only the low-side transistor switch worked. After consulting few electrical engineers, he found out that he used wrong transistor. In the first place, TIP120 is a NPN Transistor, to use as a switch, it should be used for LOW-SIDE SWITCH, not high-side switch. For high-side switch, a mosfet that is PNP configuration should be used instead. However, for high-side switch to switch on 24VDC, a high voltage of at least 12VDC needs to be used, the Raspberry Pi can only send out 5VDC as signal, thus, another PNP high-side switch transistor has to be used. 

For this application, a relay should be used instead. Wen Da spent the rest of the day drawing the Relay circuit for high-side switch. The first PCB can be used for low-side switch. Wen Da learned how to make his own EAGLE library using this youtube video: [https://www.youtube.com/watch?v=yvRGmltr_P8](https://www.youtube.com/watch?v=yvRGmltr_P8)

This was required as the Fablab's 2xterminal block was not a standard part and there were troubles aligning the holes of the first PCB with the fablab's terminal block. Thus, Wen Da made an EAGLE library with the terminal block of 4.5mm pitch that fit with the fablab's terminal block.

![](https://raw.githubusercontent.com/wendahere/GoGetter/master/Electrical%20Component/PCB%20Etching/Electrical%20PCB/Part2/EAGLE.JPG)

However, the (left side) schematic was not done very well, the holes could not be seen unless the mouse hover over it. The PCB (right side) however, was good as the spacing was accurately measured using a vernier caliper. 

### Wednesday 04/11/2020

Allen made some adjustments to the height of the vending machine frame, and went to measure the stands of existing vending machine, where he found that they are between 3 inches to 6 inches. Therefore, the final height of the vending machine frame is 1600mm, and the stands to use is 100mm, which will bring the final height of the vending machine to be 1700mm. 

Allen also did 2D drawings for the panels for the vending machine frame. 

Wen Da brought some blind rivets and a rivet gun for Allen to familiarise on how to do riveting.

![](https://raw.githubusercontent.com/wendahere/GoGetter/master/Electrical%20Component/PCB%20Etching/Electrical%20PCB/Part2/E4CC2EA4-E43A-4CEF-8890-15213081BFE4.jpg)

Allen prepared some aluminium pieces to practice on how to rivet. 

Wen Da printed the PCB Drawing on paper to check if the copper board could fit the design Wen Da made. The drawing could not fit and Wen Da removed some terminal blocks and moved the components closer and it fit well.

Below are the steps on how to make high resolution print for PCB on Special paper for heat press: (This was learned from SP Fab Academy's Ting: [http://fabacademy.org/2020/labs/singapore/students/engting-kok/exercise06.html](http://fabacademy.org/2020/labs/singapore/students/engting-kok/exercise06.html) )

1. Only show the layers that you want to print, in my case, I wanted top, pads and tnames.
 ![](https://raw.githubusercontent.com/wendahere/GoGetter/master/Electrical%20Component/PCB%20high%20res%20printing/Screenshot%20(39).png)
2. Go File>Export>Image 
![](https://raw.githubusercontent.com/wendahere/GoGetter/master/Electrical%20Component/PCB%20high%20res%20printing/Screenshot%20(33).png)
3. Set Resolution to 1000dpi and Click Monochrome 
![](https://raw.githubusercontent.com/wendahere/GoGetter/master/Electrical%20Component/PCB%20high%20res%20printing/Screenshot%20(34).png)
4. Import the image to any software that can mirror and invert colors, I used Inkscape 
![](https://raw.githubusercontent.com/wendahere/GoGetter/master/Electrical%20Component/PCB%20high%20res%20printing/Screenshot%20(35).png)
5. Go Path>Trace Bitmap ![](https://raw.githubusercontent.com/wendahere/GoGetter/master/Electrical%20Component/PCB%20high%20res%20printing/Screenshot%20(36).png)
6. Click on Invert Image then OK 
![](https://raw.githubusercontent.com/wendahere/GoGetter/master/Electrical%20Component/PCB%20high%20res%20printing/Screenshot%20(37).png)
7. Remove the initial image 
![](https://raw.githubusercontent.com/wendahere/GoGetter/master/Electrical%20Component/PCB%20high%20res%20printing/Screenshot%20(38).png)
8. Mirror the image 
![](https://github.com/wendahere/GoGetter/blob/master/Electrical%20Component/PCB%20high%20res%20printing/Screenshot%20(41).png)
9. Print/Save as PDF and print on the special paper 
![](https://raw.githubusercontent.com/wendahere/GoGetter/master/Electrical%20Component/PCB%20high%20res%20printing/Screenshot%20(43).png)

Wen Da's initial print on paper was a fail as the image was too close to the edge to print.
![](https://raw.githubusercontent.com/wendahere/GoGetter/master/Electrical%20Component/PCB%20Etching/Electrical%20PCB/Part2/IMG_5357.JPG)

After editing and checking, Wen Da printed the image on the special glossy paper and cut and pasted on the copper board using Kepton tape.

![](https://raw.githubusercontent.com/wendahere/GoGetter/master/Electrical%20Component/PCB%20Etching/Electrical%20PCB/Part2/IMG_5358.JPG)

Ready the chemical solution and etch!
![](https://raw.githubusercontent.com/wendahere/GoGetter/master/Electrical%20Component/PCB%20Etching/Electrical%20PCB/Part2/IMG_5360.JPG)

The first etch was a fail, for some reason, there was some black residue and the black protection corroded off as well.

![](https://raw.githubusercontent.com/wendahere/GoGetter/master/Electrical%20Component/PCB%20Etching/Electrical%20PCB/Part2/8BF64C5D-5433-477E-A70B-6E610AA636F3.jpg)

After consulting and asking around, Wen Da learned that it was because the glossy special paper was slightly crumpled when Wen Da printed his board on it. The special glossy paper rolls up when exposed to the atmosphere for too long. Wen Da had to be quick and print once opened the paper.

After etching, there was a large problem. Although the board was dull and similar to the first PCB board made, the most parts of the PCB still had continuity! Wen Da learned the reason was because the copper board was left exposed to the atmosphere for too long and the oxidation protected the copper board from the chemicals. After using a smoother type sand paper and sanding away the oxidation, there was obvious copper left. Wen Da with help from Fablab Technician Louis, used an Exacto Knife and scrapped away the portions that still had continuity. 

Wen Da went home and used a dremel tool to remove away most of the extra copper.

![](https://raw.githubusercontent.com/wendahere/GoGetter/master/Electrical%20Component/PCB%20Etching/Electrical%20PCB/Part2/801D1F7E-2DA1-413B-AA82-9073E4F60950.jpg)

**show pictures**

Allen calculated the rough weight of the feed tray to determine the load the drawer rollers will have to support. Here are the calculations: 

- Feed tray weight (2mm 5083 aluminium): 0.99kg [calculated using [this website](http://www.aalco.co.uk/online-tools/weight-calculator/)]
- Feed tray weight (1mm maraging steel): 1.55kg [caclulated using [this website](http://www.aalco.co.uk/online-tools/weight-calculator/)] 
- Coil weight: 0.33 * 5 = 1.65kg
- Motor weight: * 5 =
- Motor bracket weight (3mm maraging steel): 0.29 * 5 = 1.45kg 
- Angle bar weight (1mm 5083 aluminium): 0.06 * 5 = 0.3kg
- Handle weight (2mm 5083 aluminium): 0.14 + 0.17 + 0.17 = 0.48kg 
- Ramp weight (2mm acrylic): 
- Prize weight (heaviest): 120 * 14 = 1.68kg 
- LED weight: 
- Fastener weight: 
- Drawer slider weight:  

Total weight (2mm aluminium): 0.99 + 1.65 + + 1.45 + 0.3 + 0.48 + + 1.68 + + + =

Total weight (1mm steel): 1.55 + 1.65 + + 1.45 + 0.3 + 0.48 + + 1.68 + + + = 

Allen also made a template for GOS on how to tie string that will be use to loop around the coil.

**show picture**

Reynard read up on SQL which will be used for the database of the students.

Wen Da designed a new board for chemical etching.

### Thursday 05/11/2020

Wen Da drilled holes in the new PCB Board and put in the components to get it ready for soldering. Wen Da worked on the Journal and report. 

![](https://raw.githubusercontent.com/wendahere/GoGetter/master/Electrical%20Component/PCB%20Etching/Electrical%20PCB/Part2/IMG_5371.JPG)

![](https://raw.githubusercontent.com/wendahere/GoGetter/master/Electrical%20Component/PCB%20Etching/Electrical%20PCB/Part2/last.JPG)

Afterwards, Wen Da and Allen went to mechanical parts hardware store at Blk 802 French Road. Allen brought back few sizes of rivets, given as sample. We looked at drawer slides and learned that they only sell ball bearing drawer slides, not wheel type drawer slides. Both drawer slides can only up to 30kk and the wheel drawer slides are cheaper.

### Friday 06/11/2020

Wen Da had an expert to help solder the PCB board and he tested it. The current draw from the motor was 60mA and current draw for the relay was 30mA.

Wen Da tested with both high-side and low-side switches boards and it works!


## Week 9 (8/11/2020 to 14/11/2020) 

### Monday 02/11/2020

Wen Da worked on final design of PCB EAGLE board to be manufactured and emailed JLCPCB about his inquiries and talked to Mr Steven Chew about PCB Vias.

Reynard worked on his keycaps.

Allen did the tray design.

### Tuesday 03/11/2020