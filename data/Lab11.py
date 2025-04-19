#!/usr/bin/env python3
import os
import sys
import matplotlib.pyplot as plt
import pygame

# ─── Constants & Paths ─────────────────────────────────────────────────────────
DATA_DIR         = 'data'
TOTAL_POINTS     = 1000
STUDENTS_FILE    = os.path.join(DATA_DIR, 'students.txt')
ASSIGNMENTS_FILE = os.path.join(DATA_DIR, 'assignments.txt')
SUBMISSIONS_FILE = os.path.join(DATA_DIR, 'submissions.txt')

# ─── Helpers ────────────────────────────────────────────────────────────────────
def check_file(fp):
    if not os.path.isfile(fp):
        print(f"Error: '{fp}' not found")
        sys.exit(1)

# ─── Load Data ─────────────────────────────────────────────────────────────────
def load_students():
    check_file(STUDENTS_FILE)
    students = {}
    with open(STUDENTS_FILE) as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            # split name and id: last whitespace-separated part is id
            try:
                name, sid = line.rsplit(None, 1)
            except ValueError:
                continue
            students[sid] = name
    return students


def load_assignments():
    check_file(ASSIGNMENTS_FILE)
    assignments = {}
    name_to_id  = {}
    with open(ASSIGNMENTS_FILE) as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            # split into name, points, id: last two parts are points and id
            try:
                rest, aid = line.rsplit(None, 1)
                name, pts_s = rest.rsplit(None, 1)
            except ValueError:
                continue
            try:
                pts = float(pts_s)
            except ValueError:
                continue
            assignments[aid]   = (name, pts)
            name_to_id[name]   = aid
    return assignments, name_to_id


def load_submissions():
    submissions = {}
    # try single file
    if os.path.isfile(SUBMISSIONS_FILE):
        files = [SUBMISSIONS_FILE]
    else:
        subdir = os.path.join(DATA_DIR, 'submissions')
        if os.path.isdir(subdir):
            files = [os.path.join(subdir, fn)
                     for fn in os.listdir(subdir) if fn.endswith('.txt')]
        else:
            print("Warning: no submissions data found")
            return submissions
    for fp in files:
        with open(fp) as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                # split student_id, assignment_id, percent
                try:
                    sid, aid, pct_s = line.split(None, 2)
                except ValueError:
                    continue
                try:
                    pct = float(pct_s)
                except ValueError:
                    continue
                if pct <= 1:
                    pct *= 100
                submissions[(sid, aid)] = pct
    return submissions

# ─── Option 1: Student Grade ────────────────────────────────────────────────────
def get_student_grade(student_name, students, assignments, submissions):
    sid = next((s for s, n in students.items() if n == student_name), None)
    if not sid:
        print("Student not found")
        return
    total_score = sum((submissions.get((sid, aid), 0) / 100) * pts
                      for aid, (_, pts) in assignments.items())
    grade_pct = round((total_score / TOTAL_POINTS) * 100)
    print(f"{grade_pct}%")

# ─── Option 2: Assignment Statistics ───────────────────────────────────────────
def assignment_statistics(assign_name, assignments, name_to_id, submissions):
    aid = name_to_id.get(assign_name)
    if not aid:
        print("Assignment not found")
        return
    scores = [p for (s,a), p in submissions.items() if a == aid]
    if not scores:
        print("Assignment not found")
        return
    print(f"Min: {int(min(scores))}%")
    print(f"Avg: {int(sum(scores)/len(scores))}%")
    print(f"Max: {int(max(scores))}%")

# ─── Option 3: Assignment Graph (Pygame) ───────────────────────────────────────
def assignment_graph(assign_name, assignments, name_to_id, submissions):
    aid = name_to_id.get(assign_name)
    if not aid:
        print("Assignment not found")
        return
    scores = [p for (s,a), p in submissions.items() if a == aid]
    if not scores:
        print("Assignment not found")
        return
    plt.clf()
    plt.hist(scores, bins=[0,25,50,75,100], edgecolor='black')
    plt.title(assign_name)
    plt.xlabel("Percent Score")
    plt.ylabel("Number of Students")
    tmp = "__hist.png"
    plt.savefig(tmp)
    pygame.init()
    img = pygame.image.load(tmp)
    w, h = img.get_width(), img.get_height()
    screen = pygame.display.set_mode((w, h))
    pygame.display.set_caption(f"{assign_name} Distribution")
    screen.blit(img, (0,0))
    pygame.display.flip()
    running = True
    while running:
        for e in pygame.event.get():
            if e.type in (pygame.QUIT, pygame.KEYDOWN):
                running = False
    pygame.quit()
    try: os.remove(tmp)
    except OSError: pass

# ─── Top-Level Execution ───────────────────────────────────────────────────────
students = load_students()
assignments, name_to_id = load_assignments()
submissions = load_submissions()
print("1. Student grade")
print("2. Assignment statistics")
print("3. Assignment graph")
choice = input("\nEnter your selection: ").strip()
if choice == '1':
    nm = input("What is the student's name: ").strip()
    get_student_grade(nm, students, assignments, submissions)
elif choice == '2':
    an = input("What is the assignment name: ").strip()
    assignment_statistics(an, assignments, name_to_id, submissions)
elif choice == '3':
    an = input("What is the assignment name: ").strip()
    assignment_graph(an, assignments, name_to_id, submissions)
else:
    print("Invalid selection")