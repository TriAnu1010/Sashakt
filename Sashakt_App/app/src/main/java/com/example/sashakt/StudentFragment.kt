package com.example.sashakt

import android.os.Bundle
import android.os.Handler
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import android.widget.Toast
import androidx.fragment.app.Fragment
import com.example.sashakt.databinding.FragmentStudentBinding


class StudentFragment : Fragment() {
    private lateinit var binding: FragmentStudentBinding

    override fun onCreateView(inflater: LayoutInflater, container: ViewGroup?, savedInstanceState: Bundle?): View? {
        binding = FragmentStudentBinding.inflate(inflater, container, false)

        binding.downloadButton.setOnClickListener{downloadResource()}
        return binding.root
    }

    private fun downloadResource(){
        Handler().postDelayed({
            Toast.makeText(getContext(), "File downloaded successfully!", Toast.LENGTH_SHORT).show()
        }, 1000)
    }
}