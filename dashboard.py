import matplotlib.pyplot as plt
import numpy as np
import os  # Added for directory handling

def create_student_dashboard():
    # Sample data
    semesters = ['Sem 1', 'Sem 2', 'Sem 3', 'Sem 4']
    marks = [75, 82, 78, 85]
    subjects = ['Math', 'Science', 'History', 'English', 'Arts']
    subject_marks = [88, 76, 82, 90, 65]
    study_time = [15, 20, 10, 25, 5]  # hours per week
    colors = ['#FF6B6B', '#4ECDC4', '#45B7D1', '#FFA07A', '#98D8C8']

    # Create figure with subplots
    fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(18, 6))
    fig.suptitle('Student Performance Dashboard', fontsize=16, y=1.05)

    # Line Chart - Semester Progress
    ax1.plot(semesters, marks, marker='o', color='#45B7D1', linewidth=2.5)
    ax1.set_title('Semester-wise Performance')
    ax1.set_xlabel('Semester')
    ax1.set_ylabel('Average Marks (%)')
    ax1.grid(True, linestyle='--', alpha=0.6)
    ax1.set_ylim(60, 100)
    
    # Add value labels
    for i, mark in enumerate(marks):
        ax1.text(i, mark+1, f'{mark}%', ha='center')

    # Bar Chart - Subject Performance
    bars = ax2.bar(subjects, subject_marks, color=colors)
    ax2.set_title('Subject-wise Marks')
    ax2.set_ylabel('Marks (%)')
    ax2.set_ylim(0, 100)
    ax2.grid(True, axis='y', linestyle='--', alpha=0.6)
    
    # Add value labels on bars
    for bar in bars:
        height = bar.get_height()
        ax2.text(bar.get_x() + bar.get_width()/2., height,
                f'{height}%',
                ha='center', va='bottom')

    # Pie Chart - Study Time Distribution
    ax3.pie(study_time, labels=subjects, colors=colors, autopct='%1.1f%%',
            startangle=90, explode=[0.05]*len(subjects), shadow=True)
    ax3.set_title('Study Time Distribution')
    ax3.axis('equal')

    # Create assets directory if it doesn't exist
    os.makedirs('assets', exist_ok=True)
    
    # Save path - using forward slashes works cross-platform
    save_path = os.path.join('assets', 'student_dashboard.png')
    
    # Adjust layout and save
    plt.tight_layout()
    plt.savefig(save_path, dpi=120, bbox_inches='tight')
    plt.show()

if __name__ == "__main__":
    create_student_dashboard()