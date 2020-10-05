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

**BOM**

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

###24/09/2020 - Site visit 1 to GOS
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


**Different tiers of rewards **

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
- Proposal to GOS 2nd week of october (5/10/20 - 9/10/20)


field research
Using Threaded Rod/Lead screw, 10mm OD, 2mm approx $2.50 each, stainless steel $10
Either cut into length and weld hexagon at one end or simply have a fixed nut in the frame to make the rod modular
Using springs, must be custom-made, 1 week lead time, approx $25 each, cost will go down for more quantity requested