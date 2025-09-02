import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';

@Component({
    selector: 'app-root',
    standalone: true,
    imports: [CommonModule, FormsModule],
    templateUrl: './app.component.html',
    styleUrl: './app.component.css'
})
export class AppComponent {
    title = 'Meine Django-Angular App';
    tasks: any[] = [
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

    toggleTask(task: any) {
        task.completed = !task.completed;
    }

    deleteTask(id: number) {
        this.tasks = this.tasks.filter(task => task.id !== id);
    }
}