# Hi, I'm Lkhanaajav Mijiddorj

**Data Scientist & Software Engineer** based in Oklahoma, US

I build at the intersection of machine learning, computer vision, and full-stack software. My undergraduate thesis was a complete autonomous navigation system for electric scooters — real hardware, real roads, no LiDAR.

---

## Thesis Project

### [Autonomous Scooter Navigation System](https://github.com/Lkhanaajav/live_test_scooter_project)

> Real-time autonomous sidewalk navigation using a single camera, running at 8 Hz on embedded hardware.

**What I built:** A full navigation stack — road segmentation with a custom fine-tuned SegFormer model, Bird's Eye View path planning via homography transform, safe corridor extraction using distance transforms, and a pure pursuit controller sending commands to the scooter over serial.

**How I trained the model:** Teacher-student approach. No labeled sidewalk data. Used OneFormer (Swin-L, Cityscapes) to generate pseudo-labels on my own video footage, then distilled into a lightweight SegFormer-B0 that runs fast enough on an ARM64 board.

**Stack:** Python · PyTorch · HuggingFace Transformers · OpenCV · SegFormer · BEV homography · EDT path planning · Rock 5B (ARM64)

**Topics:** `autonomous-navigation` `semantic-segmentation` `bird-eye-view` `path-planning` `deep-learning` `robotics`

---

## Other Projects

| Project | Description | Stack |
|---|---|---|
| [NarHotel](https://github.com/Lkhanaajav/NarHotel) | Full-stack hotel management web app | TypeScript |
| [Lab Monitor](https://github.com/Lkhanaajav/Lab_Monitor_time) | Lab access monitoring with auth + audit logging | Python |
| [Campus Scheduler](https://github.com/Lkhanaajav/SchedulerSoftwareProject) | Django REST API for campus event booking | Python, Django |
| [gstack fork](https://github.com/Lkhanaajav/gstack) | Added full/medium/low mode system, reduces preamble token cost ~80% | Bash, Markdown |
| [R Stats Package](https://github.com/Lkhanaajav/LhanaaPackage) | Custom R package: bootstrapping, max likelihood, ticket modeling | R |

---

## Skills

**Languages:** Python · TypeScript · JavaScript · R · C

**ML / CV:** SegFormer · HuggingFace Transformers · PyTorch · OpenCV · semantic segmentation · BEV · path planning

**Web:** Django · React · REST APIs

**Tools:** Git · SQLite · Linux · embedded systems

---

## GitHub Stats

![GitHub Stats](https://github-readme-stats.vercel.app/api?username=Lkhanaajav&show_icons=true&theme=default&hide_border=true)
![Top Languages](https://github-readme-stats.vercel.app/api/top-langs/?username=Lkhanaajav&layout=compact&theme=default&hide_border=true)

---

**Email:** lhanaamijgee@gmail.com