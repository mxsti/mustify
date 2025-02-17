import {Component, inject, OnInit} from '@angular/core';
import {RouterModule} from '@angular/router';
import {SongService} from '../song.service';
import {SongInfo} from '../song.model';
import {NgForOf} from '@angular/common';
import {environment} from '../../../environments/environment.development';

@Component({
  selector: 'app-song-info-page',
  imports: [RouterModule, NgForOf],
  templateUrl: './song-info-page.component.html',
  styleUrl: './song-info-page.component.css'
})
export class SongInfoPageComponent implements OnInit {
  private songService =  inject(SongService);
  private baseUrl = environment.baseUrl;
  playingSong = false;
  currentSong: string | undefined = undefined;
  songsInfo: SongInfo[] = [];

  ngOnInit() {
    this.songService.getSongsInfo().subscribe((songInfo) => {
      this.songsInfo = songInfo;
      console.log(this.songsInfo);
    });
  }

  playSong(fileName: string){
    this.playingSong = true;
    this.currentSong = `${this.baseUrl}/songfiles/${fileName}`;
  }
}
