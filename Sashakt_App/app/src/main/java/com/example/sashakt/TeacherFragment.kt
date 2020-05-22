package com.example.sashakt

import android.os.Bundle
import android.os.Handler
import androidx.fragment.app.Fragment
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import android.widget.TextView
import android.widget.Toast
import com.example.sashakt.databinding.FragmentTeacherBinding

class TeacherFragment : Fragment() {

    override fun onCreateView(
        inflater: LayoutInflater,
        container: ViewGroup?,
        savedInstanceState: Bundle?
    ): View? {
        val binding = FragmentTeacherBinding.inflate(inflater, container, false)
        context ?: return binding.root

        binding.uploadButton.setOnClickListener { uploadResource() }
        return binding.root
    }

    private fun uploadResource() {
        Handler().postDelayed({
            Toast.makeText(getContext(), "File uploaded successfully!", Toast.LENGTH_SHORT).show()
        }, 1000)
    }
}
