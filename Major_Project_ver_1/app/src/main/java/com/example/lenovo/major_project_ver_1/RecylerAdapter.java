package com.example.lenovo.major_project_ver_1;

import android.content.Intent;
import android.support.v7.view.menu.MenuView;
import android.support.v7.widget.RecyclerView;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.ImageView;
import android.widget.TextView;

/**
 * Created by Lenovo on 28-02-2018.
 */

public class RecylerAdapter extends RecyclerView.Adapter<RecylerAdapter.ViewHolder> {

    private String[] Titles = {"Take Drunk Test","Track Location"};
    private int[] images = {R.drawable.img3,R.drawable.img5};


    class ViewHolder extends  RecyclerView.ViewHolder{
        public  int currentItem;
        public ImageView itemImage;
        public TextView itemTitle;

        public ViewHolder(final View itemView) {
            super(itemView);
            itemImage = itemView.findViewById(R.id.item_image);
            itemTitle = itemView.findViewById(R.id.item_title);
            itemView.setOnClickListener(new View.OnClickListener() {
                @Override
                public void onClick(View view) {
                    int postion = getAdapterPosition();
                    if(postion == 0)
                    {
                        Intent intent = new Intent(itemView.getContext(),QuizActivity.class);
                        itemView.getContext().startActivity(intent);
                    }
                    else {
                        Intent intent = new Intent(itemView.getContext(),LocationTrackerActivity.class);
                        itemView.getContext().startActivity(intent);
                    }
                }
            });


        }
    }
    @Override
    public RecylerAdapter.ViewHolder onCreateViewHolder(ViewGroup parent, int viewType) {
        View view = LayoutInflater.from(parent.getContext()).inflate(R.layout.card_layout,parent,false);
        ViewHolder viewHolder = new ViewHolder(view);
        return viewHolder;
    }

    @Override
    public void onBindViewHolder(RecylerAdapter.ViewHolder holder, int position) {
        holder.itemTitle.setText(Titles[position]);
        holder.itemImage.setImageResource(images[position]);

    }

    @Override
    public int getItemCount() {
        return Titles.length;
    }
}
