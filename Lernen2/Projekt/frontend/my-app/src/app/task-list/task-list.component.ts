import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';

@Component({
    selector: 'app-task-list',
    standalone: true,
    imports: [CommonModule, FormsModule],
    templateUrl: './task-list.component.html',
    styleUrl: './task-list.component.css'
})
export class TaskListComponent {
    tasks = [
        { id: 1, title: 'Angular lernen', completed: false },
        { id: 2, title: 'Django API verbinden', completed: false }
    ];
    newTask = '';

    addTask() {
        if (this.newTask.trim()) {
            this.tasks.push({
                id: this.tasks.length + 1,
                title: this.newTask,
                completed: false
            });
            this.newTask = '';
        }
    }
}