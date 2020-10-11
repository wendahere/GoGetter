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
- Prize collection function - design E (backup C+D)
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

After doing further research, we decided to move our focus away from springs for the dispensing mechanism. This is because, we have found out that the springs we need have to be custom manufcatured, which means that they are expensive and not easily obtainable. We didn't want this as we wanted the standard parts that could be easily bought off the shelf, and require little to zero adjustments/machining. This is so, if any part fail during operation, GOS could easily maintain the machines by themselves, by ordering a replacement part online and replacing said part. Therefore, instead of using springs, we decided to switch to either using a threaded rod or lead screw driven by a stepper motor to dispense the prize instead. It still keeps the original design concept (prizes are hooked onto a rod). We also found that it will be easier for GOS to maintain the machine in the long run. Furthermore, the overall cost would be cheaper too. 

#### Concpet Sketches

Allen came up with some preliminary sketches on some of the main functions, so that the team have an idea how the final design would potentially look like. 

Layout planning for the vending machine:

<img src="https://raw.githubusercontent.com/wendahere/GoGetter/master/Images/Layout%20planning.jpg" alt="Layout planning" style="width:100%; height:100%;">

Different designs of the NFC card reader:
![Card reader](https://raw.githubusercontent.com/wendahere/GoGetter/master/Images/Card%20reader.jpg)

Different views of the prize dispensing function
![Dispensing](https://raw.githubusercontent.com/wendahere/GoGetter/master/Images/Dispensing.jpg)

![Dispensing 2](https://raw.githubusercontent.com/wendahere/GoGetter/master/Images/Dispensing%202.jpg) 

#### Dirty Prototype

A shoebox was used to make a dirty prototype of the vending machine, it helped to visualise where the different components will be located, and how will they be physically mounted on to the body of the vending machine. This is a quick, easy and inexpensive way for us to see whether the design ideas we decided during the conceive stage will be feasible.

Dirty prototype:

<img src="https://raw.githubusercontent.com/wendahere/GoGetter/master/Images/DP_external%201.jpg" alt="DP_external" width="49%"> <img src="https://raw.githubusercontent.com/wendahere/GoGetter/master/Images/DP_internals%20(empty).jpg" alt="DP_internals(empty)" width="49%">

![](https://raw.githubusercontent.com/wendahere/GoGetter/master/Images/DP_internals.jpg)

<img src="https://raw.githubusercontent.com/wendahere/GoGetter/master/Images/DP_internals.jpg" alt="DP_internals" height="50">

<img src="https://raw.githubusercontent.com/wendahere/GoGetter/master/Images/DP_internals.jpg" alt="DP_internals" style="height: 500px;">

### Tuesday 6/10/2020
Allen used Inventor to draw out the 3D prototype. Wen Da did circuit drawings. 

We decided to use a Power Supply Unit (PSU), rated AC input 220v +-15%, DC Output 12v, 15A. Since the RaspberryPi only requires 5v and about 2A max input, we are able to step down the 12V to 5V using a 7805 transistor. We are also putting a fuse at 12v (from PSU) side connected to the stepper motor driver. There is no fuse at the 5v RaspberryPi as the fuse has an extremely low chance to be blown. We are also putting capacitor in parallel at 12v and 5v from the PSU. We are using 24v rated capacitor at the 12v side and 10v rated capacitor at the 5v side. It is standard practice to double the capacitor size of voltage required.

Below is image of circuit sketch.
![sketch](https://raw.githubusercontent.com/wendahere/GoGetter/master/Images/circuit%20sketch.JPG)

Image of PSU we are using:
![PSU](https://raw.githubusercontent.com/wendahere/GoGetter/master/Images/psu3.JPG)

#### Inventor CAD


### Wednesday 7/10/2020
Allen and Reynard worked together to laser cut and 3D print to fabricate first prototype.
Wen Da worked more on circuit. We tested the 7805 transistor using a power supply to check that it is working. Wen Da soldered the working 7805 on a copper stripboard with red and black wires to connect the PSU to the RaspberryPi. 

We are considering on using a Single Pole Double Throw Relay to reduce the amounts of stepper motor drivers required to cut down on cost.

This is how the circuit will look like:

![](https://raw.githubusercontent.com/wendahere/GoGetter/master/Images/SPDT.JPG)

Testing of 7805 transistor (12v from power supply step down to 5v)
![transtest](https://raw.githubusercontent.com/wendahere/GoGetter/master/Images/transistortest.PNG)

Soldered Stripboard

![](https://raw.githubusercontent.com/wendahere/GoGetter/master/Images/stripboard.JPG)

(insert allen/reynard prototyping part)


### Wednesday 7/10/2020

Wen Da drew out circuit diagram for having Double Pole, Double Throw Relay (DPDT). After much consultation with electrical experts, we decided to use one fuse (about 10-12A) after the PSU steps down from 220v to 12v. This is because there is a fuse at the plug for the PSU. After stepping down, only 1 fuse is required. There is no need for each stepper motor to have it's own fuse. Afterwards, Wen Da went Sim Lim Tower to buy fuse holder, fuses and 4 pin wire. Wen Da also sent out emails for sponsorships.

![](https://raw.githubusercontent.com/wendahere/GoGetter/master/Images/WithDPDT.JPG)

Allen and Reynard laser cut cardboard for the prototype. We then glued and assembled the prototype. 
Reynard 3D printed the parts for the prototype.

1st design of the collection point didn’t work - cuz the linkages 

## put images


### Thursday 8/10/2020

Wen Da sent out more sponsorship emails.
We used Arduino to test the stepper motor as the Pi was very difficult and required more time. We followed this site 
[https://howtomechatronics.com/tutorials/arduino/how-to-control-stepper-motor-with-a4988-driver-and-arduino/](https://howtomechatronics.com/tutorials/arduino/how-to-control-stepper-motor-with-a4988-driver-and-arduino/ "Guide Link")

![aa](https://raw.githubusercontent.com/wendahere/GoGetter/master/Images/teststepper.JPG)

The circuit worked well initially but then white smoke starting to form near the motor driver. It turned out that the capacitor was placed in the wrong polarity. The capacitor was burnt, this was checked by using a Digital Multimeter, setting to resistance and having 0 resistance showed that the capacitor is burnt.

After changing the capacitor, the stepper is moving accordingly to the code. We measured the amperage of the entire circuit. This was done by setting the Multimeter to ampere and putting the pins parallel to the power supply. The total draw was 1.25mA. The current draw from the A4988 stepper driver is 0.38mA. However, the draw from the stepper motor is not 12.5mA minus 0.38mA as there was no load on the stepper while it was operating. In order to find out the max current draw, we have to put on the max load required.

After installing the threaded road (load), we tested the current draw and it was the same. This is because the load is not very high, thus the current draw remained the same.

![](https://raw.githubusercontent.com/wendahere/GoGetter/master/Images/withload.JPG)

However, for power calculation, we have to use Max Load, which is the Rated Value given. This is in case anything unexpected happens, such as sudden reversing, will require the rated value.

#Assembly of prototype, keypad, monitor etc

### Friday 9/10/2020

We had a reply for the sponsorship email from a company called ShiokPizza.

##09/10/2020 - Team meeting 7 (10:00am)
We met up with Mr Soh to go through our prototype.

Use lead screws from misumi, more course, more expensive but larger gaps.

Changed from controller PLC to Pi.

Don’t have to show 3D CAD model, show prototype as we have done it. 

Can claim money if any used for prototype. 

Can be more hardy string such as nylon. Plastic string, fishing line can consider. String must be robust. How they attach the prize must think through, everything must be fuss free. 

Limitation in how much prizes GOS can hang.

Have to prescribe where they can hang the prizes. Have drop sensor to make prize dispenser more foolproof. Can use proximity sensor. 

## Going through function by function:
Have to change function names.
 
### Points ID: 

Prototype don’t have. Mr Soh likes the idea of RFID slot for students to locate where to put the card. 

LED will change color after points deducted.

### Input Function: 

Keypad, Prize is labeled. 

Press which prize desired. What happens when anyhow type? 

Must have some logic, enter and backspace.

### Prize Dispensing function: 

Stepper drive lead screw. 

Good to have support (bearing). Have to see real size if it works. 

Lead screw is heavy.

Maintenance, have to remove coupling, have to consider.

### Storage function: 

Use drawer to pull out to restock. Intend to have 3 tiers for 3 tiers of prizes. Should fix it for them, number of tiers.

Must have features to make it easy to pull out.

Wheel and rail is good, standard part is good. 

Must be limit on how far drawer can be pulled, must put a stopper. 

May consider straighten steel, weld to make drawer. Allen’s labeling as pull out is good as it is highly integrated. 

Must have good housing for all the wires, as there will be many wires. Try to be neat for maintenance. Try to be like Steve Jobs, even if can’t see, have to be neat.

### Prize Collection: 

Using 3 Bar linkage (Considered 4 bar linkage concept). 

Collection have to be with the door. 

It is good as it is highly integrated. Drop sensor can put on the wall, does not have to be on the door. 

Depending on what material we choose, the door will cost quite a lot of money. 
Prize collection will have funnel to ensure accurate dropping into collection.

### Coin dispensing: 

Bag prize with coin is good.

Sensory feedback: Can put speakers, low cost. 

Reminder to do BOM. Listen to stakeholder first before doing the BOM and standard parts.

### Security: 

Have T handle lock.
Can use bigger hinges. If got budget, can buy aluminium profile hindge to buy as standard accessories. Can go to machine design center (AMC) see their industrial hinges. 
Possible to use door hindge.


### Extra:

Cantilever design, might be too heavy. Consider them by using string, can have many types of prizes, shapes etc.

Sheet metal bending might be expensive depending on design. Better to be flat. Everytime metal is bending, it will stiffen. 

Glass cover will use either poly-carbonate or plexiglass. 

If sheet metal is flimsy, can do welding along the breath side. 

Thickness of sheet metal not considered yet. Steel hollow tube along the frame welded. Make frame out of hollow tube (eg. table legs) don’t have to use sheet metal. Have quarter inch of hollow tube is enough. 

If don’t mind having nut sticking out, can use acorn nut or rivets. 



If got money, can everything use aluminum.

Can put flagging, to tell computer if a row is depleting. 

### Sponsor: 

Break down of expenses. Write down now much money we request. Then remaining money we will consult the sponsors on what to do.

### For presentation: 

Let them see the actual moving, see the drop of the prize. 

Most important to show the functions. 

Have more drawers to show array of 3 by 3. 

Like idea of making keypad written GOS. Prototype don’t need cover on top.

Don’t need powerpoint slides, show and tell is enough. If some concepts cannot show, presentation slides can show. 

We let GOS confirm functions first, fabrication let supplier quote. Possible to bend metal to not have hollow tube but still will be flimsy, prefer to have supports. 

##Sponsorship 

Wen Da talked to ShiokPizza. They are willing to support us as they have supported SP Business School in the past. They are very open to let us visit and learn. We are planning to visit their premises and learn from their machines. Getting money will be secondary. They asked if we are building from scratch or building from a current model. As we are doing as a FYP, we are building the vending machine from scratch.

## Progress

Wen Da and Reynard finished up soldering the Voltage Regulator. As the specified capacitor was not available, we decided to use higher capacitance.

![voltageregu](https://raw.githubusercontent.com/wendahere/GoGetter/master/Images/12vto5vwithcap.JPG)

We tested the Voltage Regulator and it is working as intended. The 12v supply will be regulated to 5v for the controller.

![test](https://raw.githubusercontent.com/wendahere/GoGetter/master/Images/7805test.JPG)

